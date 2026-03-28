# Matplotlib Troubleshooting Guide

**After this lesson:** you can explain the core ideas in “Matplotlib Troubleshooting Guide” and reproduce the examples here in your own notebook or environment.

Use this page when code runs but plots look wrong, fail to display, or raise backend errors. Pair it with [Matplotlib basics](matplotlib-basics.md) for API context.

> **Tip:** Most “nothing shows” issues in notebooks are fixed with **inline mode** and **plt.show()** (see below).

## Helpful video

Context for how visualization fits into analytics and communication.

<iframe width="560" height="315" src="https://www.youtube.com/embed/RBSUwFGa6Fk" title="What is Data Science?" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Common Issues and Solutions

### 1. Display Problems

#### Plot Not Showing

Think of this as your TV not turning on:

**Purpose:** Know why a figure might not render in a script or notebook, and fix it with an explicit draw/show path or inline mode.

**Walkthrough:** `plt.show()` flushes the GUI event loop; `%matplotlib inline` embeds figures in Jupyter outputs; order matters (build the plot, then show).

```python
#  Problem: Your plot is invisible
plt.plot([1, 2, 3], [1, 2, 3])
# Nothing appears

#  Solution 1: Add plt.show() - like pressing the power button
plt.plot([1, 2, 3], [1, 2, 3])
plt.show()

#  Solution 2: For Jupyter - like setting up your TV
%matplotlib inline
plt.plot([1, 2, 3], [1, 2, 3])
```

#### Backend Issues

Think of this as your TV not being connected properly:

**Purpose:** Run Matplotlib on a machine without a display (servers, CI, SSH) by selecting a non-interactive backend before `pyplot` initializes.

**Walkthrough:** `matplotlib.use('Agg')` must run before `import matplotlib.pyplot as plt`; `Agg` renders to a buffer/file instead of opening a window.

```python
#  Error: No display name and no $DISPLAY environment variable
#  Solution: Switch to non-interactive backend - like using a different TV input
import matplotlib
matplotlib.use('Agg')  # Before importing pyplot
import matplotlib.pyplot as plt
```

### 2. Layout Problems

#### Overlapping Elements

Think of this as trying to fit too many things in a small room:

**Purpose:** Reduce label overlap and clipping by giving the figure more space and letting Matplotlib auto-adjust margins.

**Walkthrough:** Larger `figsize`, `labelpad` on axis labels, and `tight_layout`/`constrained_layout` fix most overlap issues.

```python
#  Problem: Cramped layout - like a crowded room
fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(data)
ax.set_xlabel('Very Long X Label')
ax.set_ylabel('Very Long Y Label')

#  Solution: Adjust layout - like rearranging furniture
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(data)
ax.set_xlabel('Very Long X Label', labelpad=10)
ax.set_ylabel('Very Long Y Label', labelpad=10)
plt.tight_layout(pad=1.5)
```

#### Subplots Spacing

Think of this as arranging pictures on a wall:

**Purpose:** Separate stacked axes vertically so titles and tick labels do not collide.

**Walkthrough:** `gridspec_kw={'hspace': ...}` passes spacing into the `GridSpec` that `subplots` creates; tune `hspace`/`wspace` until labels clear.

```python
#  Problem: Overlapping subplots - like pictures too close together
fig, (ax1, ax2) = plt.subplots(2, 1)

#  Solution: Add spacing - like adding space between pictures
fig, (ax1, ax2) = plt.subplots(2, 1, 
                              height_ratios=[1, 1],
                              gridspec_kw={'hspace': 0.3})
```

### 3. Data Handling

#### Missing Data

Think of this as having gaps in your story:

**Purpose:** Keep plotting functions from propagating NaNs into broken lines or empty axes by filtering or interpolating first.

**Walkthrough:** List comprehension drops NaNs; `np.interp` fills gaps using neighboring valid points along the index.

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight python %}
#  Problem: NaN values breaking plot - like missing pages in a book
data = [1, 2, np.nan, 4, 5]

#  Solution 1: Filter NaN - like skipping missing pages
clean_data = [x for x in data if not np.isnan(x)]

#  Solution 2: Interpolate - like filling in the missing parts
def handle_missing(data):
    """Handle missing values with interpolation"""
    data = np.array(data)
    mask = np.isnan(data)
    data[mask] = np.interp(
        np.flatnonzero(mask),
        np.flatnonzero(~mask),
        data[~mask]
    )
    return data
{% endhighlight %}

</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-2" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Problem Setup</span>
    </div>
    <div class="code-callout__body">
      <p>A list with a <code>np.nan</code> in position 3—plotting this directly breaks line continuity.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="4-5" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Filter Approach</span>
    </div>
    <div class="code-callout__body">
      <p>List comprehension drops NaN values entirely—fast but loses the original index positions.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="7-17" data-tint="3">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Interpolation Approach</span>
    </div>
    <div class="code-callout__body">
      <p><code>np.interp</code> fills each NaN using neighboring valid values, preserving the original array length and index alignment.</p>
    </div>
  </div>
</aside>
</div>

#### Scale Issues

Think of this as trying to compare very different things:

**Purpose:** Plot series with very different magnitudes without misleading the reader—either twin axes or normalized units.

**Walkthrough:** `twinx()` shares x but draws a second y-axis; normalization maps each series to [0, 1] for overlay comparison.

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight python %}
#  Problem: Different scales making plot unreadable - like comparing inches and miles
x = np.linspace(0, 1, 100)
y1 = x
y2 = 1000 * x

#  Solution 1: Secondary Y-axis - like using two different rulers
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.plot(x, y1, 'b-', label='y1')
ax2.plot(x, y2, 'r-', label='y2')

#  Solution 2: Normalize data - like converting everything to the same unit
def normalize(data):
    """Normalize data to [0, 1] range"""
    return (data - np.min(data)) / (np.max(data) - np.min(data))
{% endhighlight %}

</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-4" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Mismatched Scales</span>
    </div>
    <div class="code-callout__body">
      <p><code>y2</code> is 1000× larger than <code>y1</code>—on a single axis, <code>y1</code> would appear flat against the bottom.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="6-10" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Twin Axis</span>
    </div>
    <div class="code-callout__body">
      <p><code>twinx()</code> creates a second y-axis that shares the x-axis, each series keeping its own scale.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="12-15" data-tint="3">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Normalization</span>
    </div>
    <div class="code-callout__body">
      <p>Min-max normalization maps any series to [0, 1], enabling direct overlay without a dual axis.</p>
    </div>
  </div>
</aside>
</div>

### 4. Memory Management

#### Memory Leaks

Think of this as leaving too many windows open on your computer:

**Purpose:** Avoid leaking figure objects when creating many plots in a loop (especially in scripts or long notebooks).

**Walkthrough:** `plt.close('all')` after `show()` releases figures; the `try`/`finally` pattern ensures cleanup even if plotting errors.

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight python %}
#  Problem: Memory growing with multiple plots - like leaving windows open
for i in range(100):
    plt.figure()
    plt.plot(data)
    plt.show()

#  Solution: Proper cleanup - like closing windows when done
def plot_with_cleanup(data):
    """Plot with proper memory management"""
    try:
        plt.figure()
        plt.plot(data)
        plt.show()
    finally:
        plt.close('all')
{% endhighlight %}

</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-5" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Memory Leak Pattern</span>
    </div>
    <div class="code-callout__body">
      <p>Each loop iteration creates a figure object but never closes it—100 figures accumulate in memory.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="7-15" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Try/Finally Cleanup</span>
    </div>
    <div class="code-callout__body">
      <p>Wrapping in <code>try/finally</code> ensures <code>plt.close('all')</code> runs even if plotting raises an exception.</p>
    </div>
  </div>
</aside>
</div>

#### Large Dataset Handling

Think of this as trying to show too many stars in the sky:

**Purpose:** Keep scatter plots responsive when `x` and `y` have millions of points by subsampling and raster-friendly rendering.

**Walkthrough:** Random subset caps point count; `alpha` and `rasterized=True` help when exporting dense scatters to vector formats.

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight python %}
#  Problem: Slow with large datasets - like trying to show every star
x = np.random.randn(1_000_000)
y = np.random.randn(1_000_000)

#  Solution: Data reduction strategies - like showing constellations instead
def plot_large_dataset(x, y, max_points=10_000):
    """Plot large datasets efficiently"""
    if len(x) > max_points:
        # Random sampling - like choosing representative stars
        idx = np.random.choice(
            len(x),
            max_points,
            replace=False
        )
        x = x[idx]
        y = y[idx]

    # Use scatter with transparency - like showing star density
    plt.scatter(x, y, alpha=0.1, rasterized=True)
{% endhighlight %}

</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-3" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Large Dataset</span>
    </div>
    <div class="code-callout__body">
      <p>One million random points—rendering all of them makes the scatter slow and the output visually saturated.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="5-15" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Random Sampling</span>
    </div>
    <div class="code-callout__body">
      <p><code>np.random.choice</code> picks <code>max_points</code> indices without replacement, slicing both <code>x</code> and <code>y</code> to match.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="17-18" data-tint="3">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Raster Rendering</span>
    </div>
    <div class="code-callout__body">
      <p><code>alpha=0.1</code> reveals density through overlap; <code>rasterized=True</code> converts the scatter to a bitmap for smaller PDF exports.</p>
    </div>
  </div>
</aside>
</div>

### 5. Style and Formatting

#### Font Problems

Think of this as trying to use a font that's not installed:

**Purpose:** Set a preferred font while falling back to a generic family if the name is unavailable on the system.

**Walkthrough:** `rcParams['font.family']` applies globally; wrapping in try/except is illustrative—production code often uses `font_manager` to list available fonts.

```python
#  Problem: Font not found - like trying to use a font you don't have
plt.rcParams['font.family'] = 'NonExistentFont'

#  Solution: Robust font handling - like having backup fonts
def set_font_safely():
    """Set fonts with fallbacks"""
    try:
        plt.rcParams['font.family'] = 'Arial'
    except:
        plt.rcParams['font.family'] = 'sans-serif'
```

#### Color Issues

Think of this as trying to read yellow text on a white background:

**Purpose:** Replace low-contrast or neon defaults with hex colors that stay readable on white backgrounds and in print.

**Walkthrough:** The dict holds named hex codes; swap `professional_colors['blue']` into `plt.plot(..., color=...)`.

```python
#  Problem: Poor color visibility - like hard-to-read colors
plt.plot(data1, color='yellow')  # Hard to see
plt.plot(data2, color='lime')    # Too bright

#  Solution: Professional color palette - like using readable colors
professional_colors = {
    'blue': '#2E86C1',
    'red': '#E74C3C',
    'green': '#2ECC71',
    'purple': '#8E44AD',
    'orange': '#E67E22'
}
```

### 6. Export and Saving

#### Resolution Problems

Think of this as taking a blurry photo:

**Purpose:** Export PNG/PDF suitable for slides or papers by controlling DPI, padding, and bounding box.

**Walkthrough:** `dpi` sets resolution; `bbox_inches='tight'` trims whitespace; `transparent=True` is useful for slides on non-white backgrounds.

```python
#  Problem: Blurry exports - like a low-resolution photo
plt.savefig('plot.png')

#  Solution: High-quality export settings - like using a better camera
def save_high_quality(fig, filename):
    """Save figure with high quality settings"""
    fig.savefig(filename,
                dpi=300,                # High DPI - like high resolution
                bbox_inches='tight',    # No cutoff - like proper framing
                pad_inches=0.1,         # Small padding - like a small border
                transparent=True)       # Transparent background - like a PNG
```

## Debugging Tools

### 1. Plot Information

Think of this as checking your car's dashboard:

**Purpose:** Inspect the current figure and axes state (size, limits, child artists) when debugging layout or memory.

**Walkthrough:** `gcf()`/`gca()` grab the active figure and axes; `psutil` is optional and only valid if you import it elsewhere.

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight python %}
def print_plot_info():
    """Print current plot information"""
    fig = plt.gcf()
    ax = plt.gca()

    info = {
        'Figure Size': fig.get_size_inches(),
        'DPI': fig.dpi,
        'Axis Limits': {
            'X': ax.get_xlim(),
            'Y': ax.get_ylim()
        },
        'Number of Artists': len(ax.get_children()),
        'Memory Usage (MB)': (
            psutil.Process().memory_info().rss /
            1024 /
            1024
        )
    }

    return info
{% endhighlight %}

</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-4" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Active Figure/Axes</span>
    </div>
    <div class="code-callout__body">
      <p><code>gcf()</code> and <code>gca()</code> grab the currently active figure and axes without needing explicit references.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="6-13" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Figure Properties</span>
    </div>
    <div class="code-callout__body">
      <p>The dict collects size, DPI, axis limits, and child artist count—useful for diagnosing layout or clipping issues.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="14-18" data-tint="3">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Memory Check</span>
    </div>
    <div class="code-callout__body">
      <p><code>psutil.Process().memory_info().rss</code> reads resident set size in bytes; dividing twice by 1024 converts to megabytes.</p>
    </div>
  </div>
</aside>
</div>

### 2. Performance Monitoring

Think of this as timing how long something takes:

**Purpose:** Measure how long plotting functions take when profiling slow notebooks or batch figure generation.

**Walkthrough:** The decorator wraps any callable; `functools.wraps` preserves metadata for introspection.

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight python %}
import time
import functools

def plot_timer(func):
    """Decorator to time plotting functions"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__} took {end-start:.2f} seconds')
        return result
    return wrapper
{% endhighlight %}

</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-2" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Imports</span>
    </div>
    <div class="code-callout__body">
      <p><code>time</code> provides wall-clock measurement; <code>functools</code> enables proper decorator metadata preservation.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="4-6" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Decorator Definition</span>
    </div>
    <div class="code-callout__body">
      <p><code>@functools.wraps(func)</code> copies the original function's name and docstring onto <code>wrapper</code> for clean introspection.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="7-13" data-tint="3">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Timing Wrapper</span>
    </div>
    <div class="code-callout__body">
      <p>Records <code>start</code> before and <code>end</code> after the call, then prints elapsed seconds before returning the original result.</p>
    </div>
  </div>
</aside>
</div>

## Best Practices

### 1. Setup Template

Think of this as having a checklist before starting:

**Purpose:** Apply one consistent style, figure size, font, and grid defaults before building a plot.

**Walkthrough:** `plt.style.use` sets a named style; `rcParams` fine-tunes fonts and grids; returns current figure/axes for further drawing.

<div class="code-explainer" data-code-explainer>
<div class="code-explainer__code">

{% highlight python %}
def setup_professional_plot():
    """Setup template for professional plots"""
    plt.style.use('seaborn')

    # Figure size and DPI
    plt.figure(figsize=(10, 6), dpi=100)

    # Font settings
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.size'] = 12

    # Grid settings
    plt.grid(True, linestyle=':', alpha=0.7)

    # Return figure and axes
    return plt.gcf(), plt.gca()
{% endhighlight %}

</div>
<aside class="code-explainer__callouts" aria-label="Code walkthrough">
  <div class="code-callout" data-lines="1-3" data-tint="1">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Style Application</span>
    </div>
    <div class="code-callout__body">
      <p><code>plt.style.use('seaborn')</code> applies a complete pre-built theme—clean backgrounds, muted palette, and subtle grid.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="5-6" data-tint="2">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Canvas Size</span>
    </div>
    <div class="code-callout__body">
      <p>10×6 inches at 100 DPI produces a clear figure for both notebook display and slide export.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="8-12" data-tint="3">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Font and Grid Defaults</span>
    </div>
    <div class="code-callout__body">
      <p><code>rcParams</code> sets global font family and size; <code>linestyle=':'</code> and <code>alpha=0.7</code> keep the grid subtle and non-distracting.</p>
    </div>
  </div>
  <div class="code-callout" data-lines="14-16" data-tint="4">
    <div class="code-callout__meta">
      <span class="code-callout__lines"></span>
      <span class="code-callout__title">Return Handles</span>
    </div>
    <div class="code-callout__body">
      <p>Returning the figure and axes lets callers add plot-specific elements directly without calling <code>gcf()</code>/<code>gca()</code> again.</p>
    </div>
  </div>
</aside>
</div>

### 2. Common Mistakes to Avoid

- Not closing figures when done
- Using inappropriate chart types
- Poor color choices
- Missing labels or context

### 3. Tips for Success

- Start with a clear purpose
- Keep it simple
- Test your visualizations
- Get feedback from others

## Next Steps

1. Practice with different plot types
2. Experiment with customization
3. Learn from others' code
4. Share your visualizations
5. Join the community

Remember: The best way to learn is by doing. Start with simple plots and gradually add complexity as you become more comfortable with Matplotlib.

## Additional Resources

### Documentation Links

- [Matplotlib documentation](https://matplotlib.org/stable/)
- [Matplotlib FAQ](https://matplotlib.org/stable/faq/index.html)
- [Matplotlib backends](https://matplotlib.org/stable/users/explain/figure/backends.html)

