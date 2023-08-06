import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from psiaudio import util

from .efr import EFR
from .util import add_default_options, DatasetManager, process_files


def process_file(filename, cb='tqdm', reprocess=False, segment_duration=0.2,
                 n_draw=10, n_bootstrap=100):
    manager = DatasetManager(filename)
    if not reprocess and manager.is_processed('psd.csv'):
        return
    manager.clear()
    cb = manager.create_cb(cb)
    cb(0)

    fh = EFR(filename)
    print(fh.analyze_efr_metadata.iloc[0])
    n_segments = fh.get_setting('duration') / segment_duration
    if n_segments != int(n_segments):
        raise ValueError(f'Cannot analyze {filename} using default settings')
    n_segments = int(n_segments)

    mic_grouped = fh.get_mic_epochs().groupby(['fm', 'fc'])
    eeg_grouped = fh.get_eeg_epochs().groupby(['fm', 'fc'])
    cal = fh.system_microphone.get_calibration()

    keys = []
    eeg_bs_all = []
    mic_bs_all = []

    n = len(eeg_grouped)
    for i, ((fm, fc), eeg) in enumerate(eeg_grouped):
        figure, axes = plt.subplots(3, 2, sharex=True, figsize=(12, 18))
        for ax1, ax2 in axes[1:]:
            ax1.sharey(ax2)

        if len(eeg) != 1:
            raise ValueError('Cannot analyze {filename} using default settings')

        mic = mic_grouped.get_group((fm, fc))
        eeg = eeg.values[0].reshape((n_segments, -1))[1:-1]
        mic = mic.values[0].reshape((n_segments, -1))[1:-1]
        mic_psd = util.psd_df(mic, fs=fh.mic.fs, window='hann').mean(axis=0)
        eeg_psd = util.db(util.psd_df(eeg, fs=fh.eeg.fs, window='hann').mean(axis=0))
        mic_spl = cal.get_db(mic_psd)

        axes[0, 0].plot(mic_spl, color='k')
        axes[0, 0].axhline(fh.level, color='lightblue')
        axes[0, 1].plot(eeg_psd, color='k')

        mic_bs = util.psd_bootstrap_loop(mic, fs=fh.mic.fs, n_draw=n_draw, n_bootstrap=n_bootstrap)
        eeg_bs = util.psd_bootstrap_loop(eeg, fs=fh.eeg.fs, n_draw=n_draw, n_bootstrap=n_bootstrap)
        mic_bs_all.append(mic_bs)
        eeg_bs_all.append(eeg_bs)
        keys.append((fm, fc))

        axes[1, 0].plot(mic_bs['psd_norm'], color='k')
        axes[1, 1].plot(eeg_bs['psd_norm'], color='k')
        axes[2, 0].plot(mic_bs['plv'], color='k')
        axes[2, 1].plot(eeg_bs['plv'], color='k')

        for ax in axes.flat:
            for i in range(1, 5):
                ls = ':' if i != 1 else '-'
                ax.axvline(60 * i, color='lightgray', ls=ls, zorder=-1)
                ax.axvline(fm * i, color='lightblue', ls=ls, zorder=-1)
            ax.axvline(fc, color='pink', zorder=-1)
            ax.axvline(fc+fm, color='pink', zorder=-1)
            ax.axvline(fc-fm, color='pink', zorder=-1)

        axes[0, 1].set_xscale('octave')
        axes[0, 1].axis(xmin=50, xmax=50e3)

        for ax in axes[-1]:
            ax.set_xlabel('Frequency (kHz)')
        axes[0, 0].set_title('Microphone')
        axes[0, 1].set_title('EEG')
        axes[0, 0].set_ylabel('Stimulus (dB SPL)')
        axes[0, 1].set_ylabel('Response (dB re 1Vrms)')
        axes[1, 0].set_ylabel('Norm. amplitude (dB re noise floor)')
        axes[2, 0].set_ylabel('Phase-locking value')

        figure.suptitle(f'{fc} Hz modulated @ {fm} Hz')
        manager.save_fig(figure, f'spectrum for {fc} Hz modulated at {fm} Hz.pdf')
        plt.close(figure)
        cb((i + 1) / n)

    eeg_bs_all = pd.concat(eeg_bs_all, keys=keys, names=['fm', 'fc'])
    mic_bs_all = pd.concat(mic_bs_all, keys=keys, names=['fm', 'fc'])
    manager.save_df(eeg_bs_all, 'EEG boostrapped.csv')
    manager.save_df(mic_bs_all, 'mic boostrapped.csv')

    fft_resolution = 1 / segment_duration
    noise_bins = np.array([-2, -1, 1, 2]) * fft_resolution

    efr = []
    for fm, df in eeg_bs_all.groupby('fm'):
        ix = pd.IndexSlice[:, :, fm+noise_bins]
        noise = df.loc[ix].groupby(['fm', 'fc']).mean().add_suffix('_noise')
        signal = df.xs(fm, level='frequency')
        harmonics = np.array([1, 2, 3, 4, 5]) * fm
        ix = pd.IndexSlice[:, :, harmonics]
        harmonics = df.loc[ix].groupby(['fm', 'fc'])[['psd', 'psd_norm']].sum().add_suffix('_harmonics')
        efr.append(pd.concat((noise, signal, harmonics), axis=1))

    figure, axes = plt.subplots(2, 2, figsize=(12, 12), sharex=True)
    efr = pd.concat(efr, axis=0).reset_index()
    manager.save_df(efr, 'EFR.csv')

    for fm, efr_df in efr.groupby('fm'):
        p, = axes[0, 0].plot(efr_df['fc'], efr_df['psd'], 'o-', label=f'{fm} Hz')
        c = p.get_color()
        axes[0, 0].plot(efr_df['fc'], efr_df['psd_noise'], ':')
        axes[0, 1].plot(efr_df['fc'], efr_df['psd_norm'], 'o-', label=f'{fm} Hz')
        axes[0, 1].plot(efr_df['fc'], efr_df['psd_norm_noise'], ':', color=c)
        axes[1, 0].plot(efr_df['fc'], efr_df['plv'], 'o-', color=c)
        axes[1, 0].plot(efr_df['fc'], efr_df['plv_noise'], ':', color=c)
        axes[1, 1].plot(efr_df['fc'], efr_df['psd_norm_harmonics'], 'o-', color=c)

    axes[0, 0].legend()
    axes[0, 0].set_xscale('octave')
    for ax in axes[1]:
        ax.set_xlabel('Frequency (kHz)')
    axes[0, 0].set_ylabel('EFR (dB re 1V)')
    axes[0, 1].set_ylabel('EFR (dB re noise floor)')
    axes[1, 0].set_ylabel('Phase-locking value (frac.)')
    axes[1, 1].set_ylabel('EFR with harmonics (dB re noise floor)')
    axes[1, 0].axis(ymin=0, ymax=1)
    manager.save_fig(figure, 'EFR.pdf')


def main_folder():
    import argparse
    parser = argparse.ArgumentParser('Summarize IEC data in folder')
    add_default_options(parser)
    args = parser.parse_args()
    process_files(args.folder, '**/*inear_speaker_calibration_chirp*',
                  process_file, reprocess=args.reprocess)


if __name__ == '__main__':
    #process_file(r'C:\Users\mmm\projects\psi1\data\data\20230127-124721 Sean Sean left 151122 1 efr_sam.zip')
    #process_file(r'C:\Users\mmm\projects\psi1\data\data\20230208-113146 Sean B018-1 left 400uM efr_sam.zip')
    process_file(r'C:\Users\mmm\projects\psi1\data\data\20230208-113941 Sean B018-1 left 400uM efr_ram.zip')
