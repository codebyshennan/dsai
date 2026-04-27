"""Generate interactive Plotly HTML widgets for module 4.1 simulations.

Produces standalone HTML files under this directory. Each is embedded in the
relevant lesson via an <iframe> with `loading="lazy"`.

Run from repo root:
    uv run python docs/4-stat-analysis/4.1-inferential-stats/assets/interactive/generate_interactive_simulations.py
"""

from pathlib import Path

import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from scipy import stats

OUT = Path(__file__).parent
SIZES = [5, 10, 30, 100, 500]
N_RESAMPLES = 1000
RNG = np.random.default_rng(42)
POP_SIZE = 10_000


def _make_populations() -> dict[str, np.ndarray]:
    return {
        "Normal (bell)": RNG.normal(50, 10, POP_SIZE),
        "Uniform (flat)": RNG.uniform(20, 80, POP_SIZE),
        "Right skew (exponential)": RNG.exponential(scale=10, size=POP_SIZE) + 30,
        "Bimodal": np.concatenate(
            [RNG.normal(35, 5, POP_SIZE // 2), RNG.normal(65, 5, POP_SIZE // 2)]
        ),
    }


def _save(fig: go.Figure, name: str) -> None:
    fig.update_layout(
        margin=dict(l=40, r=20, t=70, b=40),
        font=dict(family="system-ui, -apple-system, sans-serif", size=12),
        paper_bgcolor="white",
        plot_bgcolor="#fafafa",
    )
    fig.write_html(
        OUT / f"{name}.html",
        include_plotlyjs="cdn",
        full_html=True,
        config={"displayModeBar": False, "responsive": True},
    )


def clt_simulation() -> None:
    """Three panels: population, one sample, sampling distribution of x̄.

    Slider controls sample size; dropdown switches the population shape.
    """
    populations = _make_populations()
    pop_names = list(populations.keys())

    fig = make_subplots(
        rows=1,
        cols=3,
        subplot_titles=(
            "Population",
            "One sample",
            "Sampling distribution of x̄ (1,000 samples)",
        ),
        horizontal_spacing=0.08,
    )

    # Frames: one per (population, sample size)
    frames = []
    initial_traces = None
    for pop_name in pop_names:
        pop = populations[pop_name]
        for n in SIZES:
            sample = RNG.choice(pop, size=n, replace=False)
            sample_means = np.array(
                [
                    np.mean(RNG.choice(pop, size=n, replace=True))
                    for _ in range(N_RESAMPLES)
                ]
            )
            traces = [
                go.Histogram(
                    x=pop,
                    nbinsx=50,
                    marker_color="#4f7cac",
                    opacity=0.75,
                    name="Population",
                    showlegend=False,
                ),
                go.Histogram(
                    x=sample,
                    nbinsx=15,
                    marker_color="#7aa874",
                    opacity=0.85,
                    name="One sample",
                    showlegend=False,
                ),
                go.Histogram(
                    x=sample_means,
                    nbinsx=30,
                    marker_color="#e07a5f",
                    opacity=0.85,
                    name="Sample means",
                    showlegend=False,
                    histnorm="probability density",
                ),
            ]
            # Normal curve overlay on panel 3
            x = np.linspace(sample_means.min(), sample_means.max(), 100)
            y = stats.norm.pdf(x, sample_means.mean(), sample_means.std())
            traces.append(
                go.Scatter(
                    x=x,
                    y=y,
                    mode="lines",
                    line=dict(color="#222", dash="dash", width=2),
                    name="Normal fit",
                    showlegend=False,
                )
            )

            frame_name = f"{pop_name}|n={n}"
            frames.append(
                go.Frame(
                    data=traces,
                    name=frame_name,
                    layout=go.Layout(
                        title_text=(
                            f"<b>{pop_name}</b> — sample size n = {n}, "
                            f"SE of mean ≈ {sample_means.std():.2f}"
                        )
                    ),
                )
            )
            if initial_traces is None:
                initial_traces = traces

    # Add initial traces (for population[0], n=30 if available, else first frame)
    for trace, col in zip(initial_traces[:3], [1, 2, 3]):
        fig.add_trace(trace, row=1, col=col)
    fig.add_trace(initial_traces[3], row=1, col=3)
    fig.frames = tuple(frames)

    # Sliders + dropdown
    n_slider_steps = []
    for n in SIZES:
        # Each slider step jumps to the frame for the currently-selected pop.
        # Plotly limitation: slider switches *frame name*; we encode (pop, n).
        # We default the slider to first pop; users switch pop via dropdown which
        # also retargets the slider via JS-free relayout: simplest = each slider
        # step jumps to a fixed frame name; the dropdown updates the slider's
        # "currentvalue" prefix and steps. Easiest: render two sliders is ugly;
        # so we use a *combined* approach — each frame is named "pop|n" and
        # the dropdown rewrites the slider steps via `args=[..., {"sliders": ...}]`.
        n_slider_steps.append(
            dict(
                method="animate",
                label=str(n),
                args=[
                    [f"{pop_names[0]}|n={n}"],
                    dict(mode="immediate", frame=dict(redraw=True, duration=0)),
                ],
            )
        )

    sliders_per_pop = {
        pop: [
            dict(
                method="animate",
                label=str(n),
                args=[
                    [f"{pop}|n={n}"],
                    dict(mode="immediate", frame=dict(redraw=True, duration=0)),
                ],
            )
            for n in SIZES
        ]
        for pop in pop_names
    }

    dropdown_buttons = []
    for pop in pop_names:
        dropdown_buttons.append(
            dict(
                method="relayout",
                label=pop,
                args=[
                    {
                        "sliders[0].steps": sliders_per_pop[pop],
                        "sliders[0].active": 2,  # default n=30
                    }
                ],
            )
        )

    fig.update_layout(
        title=f"<b>{pop_names[0]}</b> — sample size n = {SIZES[2]}",
        sliders=[
            dict(
                active=2,  # n=30 default
                currentvalue=dict(prefix="Sample size n = ", font=dict(size=14)),
                pad=dict(t=40),
                steps=sliders_per_pop[pop_names[0]],
            )
        ],
        updatemenus=[
            dict(
                type="dropdown",
                direction="down",
                showactive=True,
                x=0.0,
                xanchor="left",
                y=1.18,
                yanchor="top",
                buttons=dropdown_buttons,
                pad=dict(r=8, t=4),
            )
        ],
        height=420,
        bargap=0.05,
    )
    fig.update_xaxes(title_text="Value", row=1, col=1)
    fig.update_xaxes(title_text="Value", row=1, col=2)
    fig.update_xaxes(title_text="Sample mean x̄", row=1, col=3)
    fig.update_yaxes(title_text="Frequency", row=1, col=1)

    _save(fig, "clt_simulation")


def se_vs_n_simulation() -> None:
    """Sampling distribution of the mean for varying n, with theoretical SE curve."""
    pop = RNG.normal(100, 15, POP_SIZE)
    pop_sd = np.std(pop, ddof=1)

    fig = make_subplots(
        rows=1,
        cols=2,
        subplot_titles=(
            "Sampling distribution of x̄",
            "Standard error vs sample size",
        ),
        column_widths=[0.6, 0.4],
        horizontal_spacing=0.1,
    )

    # Theoretical SE curve (right panel) — added once, never changes
    n_grid = np.arange(2, 501)
    se_grid = pop_sd / np.sqrt(n_grid)
    fig.add_trace(
        go.Scatter(
            x=n_grid,
            y=se_grid,
            mode="lines",
            line=dict(color="#4f7cac", width=2),
            name="Theoretical SE = σ/√n",
            showlegend=True,
        ),
        row=1,
        col=2,
    )

    frames = []
    initial_hist = None
    initial_marker = None
    for n in SIZES:
        means = np.array(
            [np.mean(RNG.choice(pop, size=n, replace=True)) for _ in range(N_RESAMPLES)]
        )
        empirical_se = means.std()
        hist_trace = go.Histogram(
            x=means,
            nbinsx=30,
            marker_color="#e07a5f",
            opacity=0.85,
            name=f"n={n}",
            showlegend=False,
        )
        marker_trace = go.Scatter(
            x=[n],
            y=[empirical_se],
            mode="markers",
            marker=dict(size=14, color="#e07a5f", line=dict(color="#7c2a26", width=2)),
            name="Empirical SE",
            showlegend=True,
        )
        if initial_hist is None:
            initial_hist = hist_trace
            initial_marker = marker_trace
        frames.append(
            go.Frame(
                data=[hist_trace, marker_trace],
                name=f"n={n}",
                traces=[1, 2],
                layout=go.Layout(
                    title_text=(
                        f"<b>n = {n}</b> · empirical SE = {empirical_se:.2f} · "
                        f"theoretical σ/√n = {pop_sd / np.sqrt(n):.2f}"
                    )
                ),
            )
        )

    fig.add_trace(initial_hist, row=1, col=1)
    fig.add_trace(initial_marker, row=1, col=2)
    fig.frames = tuple(frames)

    fig.update_layout(
        title=f"<b>n = {SIZES[2]}</b>",
        sliders=[
            dict(
                active=2,
                currentvalue=dict(prefix="Sample size n = ", font=dict(size=14)),
                pad=dict(t=40),
                steps=[
                    dict(
                        method="animate",
                        label=str(n),
                        args=[
                            [f"n={n}"],
                            dict(mode="immediate", frame=dict(redraw=True, duration=0)),
                        ],
                    )
                    for n in SIZES
                ],
            )
        ],
        height=400,
        bargap=0.05,
    )
    fig.update_xaxes(title_text="Sample mean x̄", row=1, col=1)
    fig.update_xaxes(title_text="Sample size n", type="log", row=1, col=2)
    fig.update_yaxes(title_text="Frequency", row=1, col=1)
    fig.update_yaxes(title_text="Standard error", row=1, col=2)

    _save(fig, "se_vs_n_simulation")


def ci_sample_size_simulation() -> None:
    """One sample at varying n; show histogram + 95% t-interval; track width."""
    mu, sigma = 100, 15
    fig = make_subplots(
        rows=1,
        cols=2,
        subplot_titles=(
            "Sample distribution with 95% CI",
            "CI width vs sample size",
        ),
        column_widths=[0.6, 0.4],
        horizontal_spacing=0.1,
    )

    # Curve of CI width vs n (theoretical, two-sided 95% t)
    n_grid = np.arange(5, 501)
    t_crit = stats.t.ppf(0.975, df=n_grid - 1)
    width_grid = 2 * t_crit * sigma / np.sqrt(n_grid)
    fig.add_trace(
        go.Scatter(
            x=n_grid,
            y=width_grid,
            mode="lines",
            line=dict(color="#4f7cac", width=2),
            name="Theoretical CI width",
            showlegend=True,
        ),
        row=1,
        col=2,
    )

    frames = []
    initial_hist = None
    initial_lower = None
    initial_upper = None
    initial_marker = None
    for n in SIZES:
        sample = RNG.normal(mu, sigma, n)
        sample_mean = sample.mean()
        sample_se = stats.sem(sample)
        lo, hi = stats.t.interval(0.95, n - 1, loc=sample_mean, scale=sample_se)

        hist = go.Histogram(
            x=sample,
            nbinsx=15,
            marker_color="#7aa874",
            opacity=0.85,
            showlegend=False,
        )
        lower = go.Scatter(
            x=[lo, lo],
            y=[0, 1],
            mode="lines",
            line=dict(color="#1f4068", dash="dot", width=2),
            yaxis="y",
            showlegend=False,
        )
        upper = go.Scatter(
            x=[hi, hi],
            y=[0, 1],
            mode="lines",
            line=dict(color="#1f4068", dash="dot", width=2),
            showlegend=False,
        )
        marker = go.Scatter(
            x=[n],
            y=[hi - lo],
            mode="markers",
            marker=dict(size=14, color="#e07a5f", line=dict(color="#7c2a26", width=2)),
            name="This sample's width",
            showlegend=True,
        )
        if initial_hist is None:
            initial_hist = hist
            initial_lower = lower
            initial_upper = upper
            initial_marker = marker
        frames.append(
            go.Frame(
                data=[hist, lower, upper, marker],
                name=f"n={n}",
                traces=[1, 2, 3, 4],
                layout=go.Layout(
                    title_text=(
                        f"<b>n = {n}</b> · CI = ({lo:.1f}, {hi:.1f}) · width = {hi - lo:.2f}"
                    )
                ),
            )
        )

    fig.add_trace(initial_hist, row=1, col=1)
    fig.add_trace(initial_lower, row=1, col=1)
    fig.add_trace(initial_upper, row=1, col=1)
    fig.add_trace(initial_marker, row=1, col=2)
    fig.frames = tuple(frames)

    fig.update_layout(
        title=f"<b>n = {SIZES[2]}</b>",
        sliders=[
            dict(
                active=2,
                currentvalue=dict(prefix="Sample size n = ", font=dict(size=14)),
                pad=dict(t=40),
                steps=[
                    dict(
                        method="animate",
                        label=str(n),
                        args=[
                            [f"n={n}"],
                            dict(mode="immediate", frame=dict(redraw=True, duration=0)),
                        ],
                    )
                    for n in SIZES
                ],
            )
        ],
        height=400,
        bargap=0.05,
    )
    fig.update_xaxes(title_text="Value", row=1, col=1)
    fig.update_xaxes(title_text="Sample size n", type="log", row=1, col=2)
    fig.update_yaxes(title_text="Frequency", row=1, col=1)
    fig.update_yaxes(title_text="95% CI width", row=1, col=2)

    _save(fig, "ci_sample_size_simulation")


def p_value_sample_size_simulation() -> None:
    """Two-sample t-test as n grows for a fixed effect size."""
    sizes = [10, 30, 100, 500, 2000]
    effect_size = 0.2  # Cohen's d
    fig = make_subplots(
        rows=1,
        cols=2,
        subplot_titles=(
            "Two groups (overlap)",
            "p-value vs sample size",
        ),
        column_widths=[0.6, 0.4],
        horizontal_spacing=0.1,
    )

    # All p-values as a curve (precomputed from same draws)
    p_curve_x, p_curve_y = [], []
    frame_data: list[tuple] = []
    for n in sizes:
        a = RNG.normal(0, 1, n)
        b = RNG.normal(effect_size, 1, n)
        _, p = stats.ttest_ind(a, b)
        p_curve_x.append(n)
        p_curve_y.append(p)
        frame_data.append((a, b, p))

    fig.add_trace(
        go.Scatter(
            x=p_curve_x,
            y=p_curve_y,
            mode="lines+markers",
            line=dict(color="#4f7cac", width=2),
            marker=dict(size=8),
            name="p-value",
            showlegend=True,
        ),
        row=1,
        col=2,
    )
    fig.add_hline(
        y=0.05,
        line_dash="dash",
        line_color="red",
        annotation_text="α = 0.05",
        row=1,
        col=2,
    )

    frames = []
    initial_a = None
    initial_b = None
    initial_marker = None
    for n, (a, b, p) in zip(sizes, frame_data):
        a_trace = go.Histogram(
            x=a,
            nbinsx=20,
            marker_color="#4f7cac",
            opacity=0.6,
            name="Group A",
            showlegend=True,
        )
        b_trace = go.Histogram(
            x=b,
            nbinsx=20,
            marker_color="#e07a5f",
            opacity=0.6,
            name="Group B",
            showlegend=True,
        )
        marker = go.Scatter(
            x=[n],
            y=[p],
            mode="markers",
            marker=dict(size=16, color="gold", line=dict(color="black", width=2)),
            name="Current n",
            showlegend=False,
        )
        if initial_a is None:
            initial_a = a_trace
            initial_b = b_trace
            initial_marker = marker
        frames.append(
            go.Frame(
                data=[a_trace, b_trace, marker],
                name=f"n={n}",
                traces=[1, 2, 3],
                layout=go.Layout(
                    title_text=(
                        f"<b>n = {n} per group</b> · effect size = {effect_size} SD · "
                        f"p = {p:.4f} ({'significant' if p < 0.05 else 'not significant'})"
                    )
                ),
            )
        )

    fig.add_trace(initial_a, row=1, col=1)
    fig.add_trace(initial_b, row=1, col=1)
    fig.add_trace(initial_marker, row=1, col=2)
    fig.frames = tuple(frames)

    fig.update_layout(
        title=f"<b>n = {sizes[1]} per group</b> · effect size = {effect_size} SD",
        barmode="overlay",
        sliders=[
            dict(
                active=1,
                currentvalue=dict(prefix="n per group = ", font=dict(size=14)),
                pad=dict(t=40),
                steps=[
                    dict(
                        method="animate",
                        label=str(n),
                        args=[
                            [f"n={n}"],
                            dict(mode="immediate", frame=dict(redraw=True, duration=0)),
                        ],
                    )
                    for n in sizes
                ],
            )
        ],
        height=420,
        bargap=0.05,
    )
    fig.update_xaxes(title_text="Value", row=1, col=1)
    fig.update_xaxes(title_text="Sample size n", type="log", row=1, col=2)
    fig.update_yaxes(title_text="Frequency", row=1, col=1)
    fig.update_yaxes(title_text="p-value", type="log", row=1, col=2)

    _save(fig, "p_value_sample_size_simulation")


def sampling_game_simulation() -> None:
    """Show 30 independent draws and which CIs cover the true mean."""
    mu, sigma = 100, 15
    n_draws = 30
    sample_n = 30

    intervals = []
    means = []
    covers = []
    for _ in range(n_draws):
        sample = RNG.normal(mu, sigma, sample_n)
        m = sample.mean()
        se = stats.sem(sample)
        lo, hi = stats.t.interval(0.95, sample_n - 1, loc=m, scale=se)
        intervals.append((lo, hi))
        means.append(m)
        covers.append(lo <= mu <= hi)

    fig = go.Figure()
    for i, ((lo, hi), m, ok) in enumerate(zip(intervals, means, covers)):
        color = "#4f7cac" if ok else "#c0625b"
        fig.add_trace(
            go.Scatter(
                x=[lo, hi],
                y=[i, i],
                mode="lines",
                line=dict(color=color, width=4),
                showlegend=False,
                hovertemplate=f"Sample {i+1}<br>CI: ({lo:.1f}, {hi:.1f})<br>Covers μ? {'Yes' if ok else 'No'}<extra></extra>",
            )
        )
        fig.add_trace(
            go.Scatter(
                x=[m],
                y=[i],
                mode="markers",
                marker=dict(color=color, size=8, symbol="circle"),
                showlegend=False,
                hoverinfo="skip",
            )
        )

    fig.add_vline(
        x=mu,
        line_dash="dash",
        line_color="red",
        annotation_text=f"True mean μ = {mu}",
        annotation_position="top",
    )

    fig.update_layout(
        title=(
            f"<b>30 independent samples, each n = {sample_n}, with 95% CI</b><br>"
            f"<sub>{sum(covers)} of 30 intervals cover the true mean (target: ~28-29 of 30 = 95%)</sub>"
        ),
        xaxis_title="Value",
        yaxis_title="Sample number",
        height=500,
        showlegend=False,
    )
    _save(fig, "sampling_game_simulation")


def power_simulation() -> None:
    """Visualize Type I, Type II, and power for a one-sided z-test on a mean.

    Shows the null distribution (centered at 0) and the alternative distribution
    (shifted by effect_size · √n). The rejection region is shaded red (Type I);
    the area of the alternative *below* the critical value is shaded orange
    (Type II / β); the area of the alternative *above* is power = 1 − β.
    """
    effect_sizes = [0.0, 0.1, 0.2, 0.3, 0.5, 0.8]  # Cohen's d values
    sample_sizes = [10, 30, 50, 100, 200, 500]
    alphas = [0.01, 0.05, 0.10]

    # Curve range: needs to cover both null and shifted alt
    z_grid = np.linspace(-4, 8, 600)

    frames = []
    initial_traces = None

    for d in effect_sizes:
        for n in sample_sizes:
            for alpha in alphas:
                shift = d * np.sqrt(n)  # non-centrality of the alt distribution
                z_crit = stats.norm.ppf(1 - alpha)

                null_pdf = stats.norm.pdf(z_grid, loc=0, scale=1)
                alt_pdf = stats.norm.pdf(z_grid, loc=shift, scale=1)

                # Power = P(Z > z_crit | alt) = 1 - Φ(z_crit - shift)
                power = 1 - stats.norm.cdf(z_crit - shift)

                # Shaded regions
                # Type I (red): null pdf to the right of z_crit
                mask_alpha = z_grid >= z_crit
                # Type II (orange): alt pdf to the left of z_crit
                mask_beta = z_grid <= z_crit
                # Power (green): alt pdf to the right of z_crit
                mask_power = z_grid >= z_crit

                traces = [
                    go.Scatter(
                        x=z_grid,
                        y=null_pdf,
                        mode="lines",
                        line=dict(color="#4f7cac", width=2),
                        name="H₀: no effect",
                        showlegend=True,
                    ),
                    go.Scatter(
                        x=z_grid,
                        y=alt_pdf,
                        mode="lines",
                        line=dict(color="#e07a5f", width=2),
                        name="H₁: real effect",
                        showlegend=True,
                    ),
                    go.Scatter(
                        x=z_grid[mask_alpha],
                        y=null_pdf[mask_alpha],
                        fill="tozeroy",
                        mode="none",
                        fillcolor="rgba(192, 98, 91, 0.5)",
                        name=f"Type I (α = {alpha})",
                        showlegend=True,
                    ),
                    go.Scatter(
                        x=z_grid[mask_beta],
                        y=alt_pdf[mask_beta],
                        fill="tozeroy",
                        mode="none",
                        fillcolor="rgba(224, 168, 88, 0.45)",
                        name=f"Type II (β = {1 - power:.2f})",
                        showlegend=True,
                    ),
                    go.Scatter(
                        x=z_grid[mask_power],
                        y=alt_pdf[mask_power],
                        fill="tozeroy",
                        mode="none",
                        fillcolor="rgba(122, 168, 116, 0.5)",
                        name=f"Power (1−β = {power:.2f})",
                        showlegend=True,
                    ),
                    go.Scatter(
                        x=[z_crit, z_crit],
                        y=[0, max(null_pdf.max(), alt_pdf.max()) * 1.05],
                        mode="lines",
                        line=dict(color="#222", dash="dash", width=1),
                        name="Critical value",
                        showlegend=False,
                    ),
                ]

                frame_name = f"d={d}|n={n}|a={alpha}"
                title = (
                    f"<b>Effect size d = {d}</b> · <b>n = {n}</b> · α = {alpha} → "
                    f"<b>power = {power:.2f}</b>"
                )
                frames.append(
                    go.Frame(
                        data=traces,
                        name=frame_name,
                        layout=go.Layout(title_text=title),
                    )
                )
                if initial_traces is None:
                    initial_traces = (traces, title)

    fig = go.Figure(data=initial_traces[0], frames=tuple(frames))
    fig.update_layout(title=initial_traces[1])

    # Three sliders: effect size, n, alpha. Each slider step jumps to a frame
    # whose name encodes (d, n, a). To avoid combinatorial slider steps, we
    # use one combined slider that steps through (d, n) at fixed α, plus a
    # dropdown for α that rebuilds the slider's frame names.
    def steps_for_alpha(alpha):
        return [
            dict(
                method="animate",
                label=f"d={d}, n={n}",
                args=[
                    [f"d={d}|n={n}|a={alpha}"],
                    dict(mode="immediate", frame=dict(redraw=True, duration=0)),
                ],
            )
            for d in effect_sizes
            for n in sample_sizes
        ]

    fig.update_layout(
        sliders=[
            dict(
                active=len(sample_sizes) * 2,  # default d=0.2, n=30
                currentvalue=dict(prefix="", font=dict(size=13)),
                pad=dict(t=40),
                steps=steps_for_alpha(0.05),
            )
        ],
        updatemenus=[
            dict(
                type="dropdown",
                direction="down",
                showactive=True,
                x=0.0,
                xanchor="left",
                y=1.18,
                yanchor="top",
                buttons=[
                    dict(
                        method="relayout",
                        label=f"α = {a}",
                        args=[
                            {
                                "sliders[0].steps": steps_for_alpha(a),
                                "sliders[0].active": len(sample_sizes) * 2,
                            }
                        ],
                    )
                    for a in alphas
                ],
                pad=dict(r=8, t=4),
            )
        ],
        height=460,
        legend=dict(orientation="h", yanchor="bottom", y=1.05, x=0.25),
        xaxis_title="Test statistic z",
        yaxis_title="Density",
    )

    _save(fig, "power_simulation")


if __name__ == "__main__":
    clt_simulation()
    se_vs_n_simulation()
    ci_sample_size_simulation()
    p_value_sample_size_simulation()
    sampling_game_simulation()
    power_simulation()
    print("Wrote interactive HTML files to", OUT)
