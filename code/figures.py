import matplotlib.pyplot as plt
from scipy.stats import t
import numpy as np
import pandas as pd
import os

import cumming_plot


def fig2(dat):
    cond = [('sp_delay0start', 'sp_delay0end', 'spacing', 3, 'C: spacing'),
            ('loc_ipsi0start', 'loc_ipsi0end', 'location_ipsilateral', 1, 'A: location ipsilateral'),
            ('loc_contra0start', 'loc_contra0end', 'location_contralateral', 2, 'B: location contralateral')]
    header = ['Condition', 'mean', '95% CI']
    x_vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    fig = plt.figure(figsize=[17 / 2.54, 6 / 2.54])
    for j, c in enumerate(cond):
        ax = fig.add_subplot(1, 3, c[3])
        start = dat[c[0]]
        end = dat[c[1]]
        slopes = list()
        intercepts = list()
        values = [[], [], [], [], [], [], [], [], [], []]
        i = 0
        for sub_start, sub_end in zip(start, end):
            vals = list(sub_start) + list(sub_end)
            eq = np.polyfit([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], vals, 1)
            slopes.append(eq[0])
            intercepts.append(eq[1])
            vals2 = list()
            if j == 0:
                for val in vals:
                    vals2.append(val + i)
            elif j == 1:
                vals2 = vals
            elif j == 2:
                for val in vals:
                    vals2.append(val * -1)
            i += 0.1
            ax.plot(x_vals, vals2, '-', color='silver', linewidth=0.5)
        mean_slope = np.mean(slopes)
        if j == 2:
            mean_intercept = np.mean(intercepts) * -1
        else:
            mean_intercept = np.mean(intercepts)
        t_val = t.ppf([0.995], len(slopes))
        slope_95 = pd.Series(slopes).sem() * t_val
        y1 = pd.Series(slopes).mean() - slope_95
        y2 = pd.Series(slopes).mean() + slope_95
        ax.plot([1, 10],
                 [1*mean_slope+mean_intercept, 10*mean_slope+mean_intercept],
                 '-k', linewidth=3)
        plt.text(-0.1, 1.15, c[4],
                 horizontalalignment='left',
                 fontsize=10,
                 transform=ax.transAxes)
        ax.set_xticks(x_vals)
        ax.set_xlabel('measure', fontsize=8)
        ax.set_xlim([1, 10])
        ax.tick_params(axis='y', which='both', labelsize=8)
        ax.tick_params(axis='x', which='both', labelsize=8)
        if j == 0:
            ax.set_ylim([0, 35])
            ax.set_ylabel('perceived spacing (cm)', fontsize=8)
        if j == 1:
            ax.set_ylim([0, 15])
            ax.set_yticks([0, 5, 10, 15])
            ax.set_ylabel('perceived location (cm)', fontsize=8)
        if j == 2:
            ax.set_ylim([0, 15])
            ax.set_yticks([0, 5, 10, 15])
            ax.set_ylabel('perceived location (cm)', fontsize=8)
    plt.tight_layout()

    fig_path = os.path.join('..', 'figures', 'fig2')
    plt.savefig(fig_path + '.pdf', format='pdf', dpi=600)
    plt.savefig(fig_path + '.png', format='png', dpi=600)
    plt.savefig(fig_path + '.svg', format='svg', dpi=600)
    plt.savefig(fig_path + '.eps', format='eps', dpi=600)


def fig3(dat):

    fig = plt.figure(figsize=[17/2.54, 15/2.54])
    style1 = {'a': ['o', 'k', 'k'], 'b': ['o', 'k', 'k'], 'diff': ['^', 'r', 'r']}
    style2 = {'a': ['o', 'k', 'k'], 'b': ['o', 'k', 'k'], 'diff': ['^', 'b', 'b']}
    style3 = {'a': ['^', 'r', 'r'], 'b': ['^', 'b', 'b'], 'diff': ['^', 'k', 'k']}
    marker_size = [1, 4]
    markeredgewdith = 1
    linewidth = 1
    ab_errors = '99%CI'
    axes_tick_width = .5
    font_size = 8
    letterfontsize = 10
    connectcolor = '0.8'
    x_spacing = [0.01, 0.015, 0.05, 0.055, 0.075]
    jit = 0.0001
    skip_raw_marker = True
    x_axis_nudge = [-0.005, -0.005, -.005]
    zero_line2 = False

    # Subplot 3,3,1  Ipsilateral delay zero
    data = [list(dat.loc_ipsi0start_mean.values),list(dat.loc_ipsi0end_mean.values)]
    ax1 = fig.add_subplot(3, 3, 1)
    cumming_plot.paired(data, ax1,
                        yticks=[0, 16, 4],
                        style=style1,
                        ylabel='Perceived location (cm)',
                        xlabel=['start', 'end', ''],
                        zero_line=False,
                        y2ticks=True,
                        ab_errors=ab_errors,
                        font_size=font_size,
                        marker_size=marker_size,
                        markeredgewidth=markeredgewdith,
                        axes_tick_width=axes_tick_width,
                        linewidth=linewidth,
                        connectcolor=connectcolor,
                        x_spacing=x_spacing,
                        jit=jit,
                        skip_raw_marker=skip_raw_marker,
                        x_axis_nudge=x_axis_nudge,
                        zero_line2=zero_line2)
    plt.text(-.125, 1.15, 'A: location ipsilateral',
             horizontalalignment='left',
             fontsize=letterfontsize,
             transform = ax1.transAxes)

    # Subplot 3,3,2  Ipsilateral delay 3min
    data = [list(dat.loc_ipsi3start_mean.values),list(dat.loc_ipsi3end_mean.values)]
    ax2 = fig.add_subplot(3, 3, 2)
    cumming_plot.paired(data,ax2,
                        yticks=[0, 16, 4],
                        style=style2,
                        xlabel=['start', 'end', ''],
                        zero_line=False,
                        y2ticks=True,
                        ylabel='Perceived location (cm)',
                        ab_errors=ab_errors,
                        font_size=font_size,
                        marker_size=marker_size,
                        markeredgewidth=markeredgewdith,
                        axes_tick_width=axes_tick_width,
                        linewidth=linewidth,
                        connectcolor=connectcolor,
                        x_spacing=x_spacing,
                        jit=jit,
                        skip_raw_marker=skip_raw_marker,
                        x_axis_nudge=x_axis_nudge,
                        zero_line2=zero_line2)

    # Subplot 3,3,3  Ipsilateral difference
    data1 = [list(dat.loc_ipsi0start_mean.values),list(dat.loc_ipsi0end_mean.values)]
    data2 = [list(dat.loc_ipsi3start_mean.values),list(dat.loc_ipsi3end_mean.values)]
    diff_zero = [end - start for start, end in zip(data1[0], data1[1])]
    diff_3min = [end - start for start, end in zip(data2[0], data2[1])]
    data = [diff_zero, diff_3min]
    ax3 = fig.add_subplot(3, 3, 3)
    cumming_plot.paired(data, ax3,
                        yticks=[-8, 8, 4],
                        style=style3,
                        xlabel=['delay\nzero', 'delay\n3 min.', ''],
                        zero_line=False,
                        y2ticks=True,
                        ylabel='Diff. perceived location (cm)',
                        ab_errors=ab_errors,
                        font_size=font_size,
                        marker_size=marker_size,
                        markeredgewidth=markeredgewdith,
                        axes_tick_width=axes_tick_width,
                        linewidth=linewidth,
                        connectcolor=connectcolor,
                        x_spacing=x_spacing,
                        jit=jit,
                        skip_raw_marker=skip_raw_marker,
                        x_axis_nudge=x_axis_nudge,
                        zero_line2=zero_line2)

    # Subplot 3,3,4  Contralateral delay zero
    data = [list(dat.loc_contra0start_mean.values), list(dat.loc_contra0end_mean.values)]
    ax4 = fig.add_subplot(3, 3, 4)
    cumming_plot.paired(data,ax4,
                        yticks=[0, 16, 4],
                        style=style1,
                        ylabel='Perceived location (cm)',
                        xlabel=['start', 'end', ''],
                        zero_line=False,
                        y2ticks=True,
                        ab_errors=ab_errors,
                        font_size=font_size,
                        marker_size=marker_size,
                        markeredgewidth=markeredgewdith,
                        axes_tick_width=axes_tick_width,
                        linewidth=linewidth,
                        connectcolor=connectcolor,
                        x_spacing=x_spacing,
                        jit=jit,
                        skip_raw_marker=skip_raw_marker,
                        x_axis_nudge=x_axis_nudge,
                        zero_line2=zero_line2)
    plt.text(-.125, 1.15, 'B: location contralateral',
             horizontalalignment='left',
             fontsize=letterfontsize,
             transform=ax4.transAxes)

    # Subplot 3,3,5  Contralateral delay 3min
    data = [list(dat.loc_contra3start_mean.values),
            list(dat.loc_contra3end_mean.values)]
    ax5 = fig.add_subplot(3, 3, 5)
    cumming_plot.paired(data, ax5,
                        yticks=[0, 16, 4],
                        style=style2,
                        xlabel=['start', 'end', ''],
                        zero_line=False,
                        y2ticks=True,
                        ylabel='Perceived location (cm)',
                        ab_errors=ab_errors,
                        font_size=font_size,
                        marker_size=marker_size,
                        markeredgewidth=markeredgewdith,
                        axes_tick_width=axes_tick_width,
                        linewidth=linewidth,
                        connectcolor=connectcolor,
                        x_spacing=x_spacing,
                        jit=jit,
                        skip_raw_marker=skip_raw_marker,
                        x_axis_nudge=x_axis_nudge,
                        zero_line2=zero_line2)

    # Subplot 3,3,6  Contralateral difference
    data1 = [list(dat.loc_contra0start_mean.values),
             list(dat.loc_contra0end_mean.values)]
    data2 = [list(dat.loc_contra3start_mean.values),
             list(dat.loc_contra3end_mean.values)]
    diff_zero = [end - start for start, end in zip(data1[0], data1[1])]
    diff_3min = [end - start for start, end in zip(data2[0], data2[1])]
    data = [diff_zero, diff_3min]
    ax6 = fig.add_subplot(3, 3, 6)
    cumming_plot.paired(data, ax6,
                        yticks=[-8, 8, 4],
                        style=style3,
                        xlabel=['delay\nzero', 'delay \n3 min.', ''],
                        zero_line=False,
                        y2ticks=True,
                        ylabel='Diff. perceived location (cm)',
                        ab_errors=ab_errors,
                        font_size=font_size,
                        marker_size=marker_size,
                        markeredgewidth=markeredgewdith,
                        axes_tick_width=axes_tick_width,
                        linewidth=linewidth,
                        connectcolor=connectcolor,
                        x_spacing=x_spacing,
                        jit=jit,
                        skip_raw_marker=skip_raw_marker,
                        x_axis_nudge=x_axis_nudge,
                        zero_line2=zero_line2)

    # subplot 3,3,7 Spacing - delay zero
    data = [list(dat.sp_delay0start_mean.values),
            list(dat.sp_delay0end_mean.values)]
    ax7 = fig.add_subplot(3, 3, 7)
    cumming_plot.paired(data, ax7,
                        yticks=[0, 30, 5],
                        style=style1,
                        ylabel='Perceived spacing (cm)',
                        xlabel=['start', 'end', ''],
                        zero_line=False,
                        y2ticks=True,
                        ab_errors=ab_errors,
                        font_size=font_size,
                        marker_size=marker_size,
                        markeredgewidth=markeredgewdith,
                        axes_tick_width=axes_tick_width,
                        linewidth=linewidth,
                        connectcolor=connectcolor,
                        x_spacing=x_spacing,
                        jit=jit,
                        skip_raw_marker=skip_raw_marker,
                        x_axis_nudge=x_axis_nudge,
                        zero_line2=zero_line2)
    plt.text(-.125, 1.15, 'C: spacing',
             horizontalalignment='left',
             fontsize=letterfontsize,
             transform=ax7.transAxes)

    # subplot 3,3,8 Spacing - delay 3min
    data = [list(dat.sp_delay3start_mean.values),
            list(dat.sp_delay3end_mean.values)]
    ax8 = fig.add_subplot(3, 3, 8)
    cumming_plot.paired(data, ax8,
                        yticks=[0, 30, 5],
                        style=style2,
                        xlabel=['start', 'end', ''],
                        zero_line=False,
                        y2ticks=True,
                        ylabel='Perceived spacing (cm)',
                        ab_errors=ab_errors,
                        font_size=font_size,
                        marker_size=marker_size,
                        markeredgewidth=markeredgewdith,
                        axes_tick_width=axes_tick_width,
                        linewidth=linewidth,
                        connectcolor=connectcolor,
                        x_spacing=x_spacing,
                        jit=jit,
                        skip_raw_marker=skip_raw_marker,
                        x_axis_nudge=x_axis_nudge,
                        zero_line2=zero_line2)

    # subplot 3,3,9 Spacing - difference
    data1 = [list(dat.sp_delay0start_mean.values),
             list(dat.sp_delay0end_mean.values)]
    data2 = [list(dat.sp_delay3start_mean.values),
             list(dat.sp_delay3end_mean.values)]
    diff_zero = [end - start for start, end in zip(data1[0], data1[1])]
    diff_3min = [end - start for start, end in zip(data2[0], data2[1])]
    data = [diff_zero, diff_3min]
    ax9 = fig.add_subplot(3, 3, 9)
    cumming_plot.paired(data, ax9,
                        yticks=[-8, 8, 4],
                        style=style3,
                        xlabel=['delay\nzero', 'delay \n3 min.', ''],
                        zero_line=False,
                        y2ticks=True,
                        ylabel='Diff. perceived spacing (cm)',
                        ab_errors=ab_errors,
                        font_size=font_size,
                        marker_size=marker_size,
                        markeredgewidth=markeredgewdith,
                        axes_tick_width=axes_tick_width,
                        linewidth=linewidth,
                        connectcolor=connectcolor,
                        x_spacing=x_spacing,
                        jit=jit,
                        skip_raw_marker=skip_raw_marker,
                        x_axis_nudge=x_axis_nudge,
                        zero_line2=zero_line2)

    # Adjust spacing of subplots
    fig.subplots_adjust(top=0.889, bottom=0.102, left=0.202, right=0.946,
                        hspace=0.571, wspace=0.758)
    plt.tight_layout()
    fig_path = os.path.join('..', 'figures', 'fig3')
    plt.savefig(fig_path + '.pdf', format='pdf', dpi=600)
    plt.savefig(fig_path + '.png', format='png', dpi=600)
    plt.savefig(fig_path + '.svg', format='svg', dpi=600)



