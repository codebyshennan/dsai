# Data Storytelling Case Studies: Learning from Real-World Examples

**After this lesson:** you can explain the core ideas in “Data Storytelling Case Studies: Learning from Real-World Examples” and reproduce the examples here in your own notebook or environment.

> **Note:** Scenarios are illustrative. Replace figure placeholders with your own screenshots when you recreate similar views in your tool of choice.

## Helpful video

Framing insights for others—related context for storytelling.

<iframe width="560" height="315" src="https://www.youtube.com/embed/RBSUwFGa6Fk" title="What is Data Science?" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Introduction: Why Case Studies Matter

Think of case studies like watching game film in sports - they show you what works, what doesn't, and how to improve. These real-world examples will help you understand how to apply data storytelling principles in practice.

## Case Study 1: Sales Performance Dashboard - Walmart's Store Analytics

### The Challenge

Walmart needed to communicate monthly sales performance to store managers across their 4,700+ US stores. The original dashboard was cluttered and confusing, making it difficult for managers to identify key performance issues and opportunities.

### The Bad Version

> **Figure (add screenshot or diagram):** A cluttered retail store dashboard with 50+ KPIs, inconsistent colors (random red/blue/green/yellow), no visual hierarchy, and metrics scattered with no logical grouping — the "before" state illustrating information overload.

**Problems Explained:**

- **Too many metrics at once**: Managers were overwhelmed with 50+ KPIs, making it impossible to focus on what mattered most
- **Inconsistent color scheme**: Random colors made it difficult to quickly identify positive vs negative trends
- **No clear hierarchy**: All metrics appeared equally important, with no visual cues for prioritization
- **Missing context**: Numbers were presented without historical comparisons or industry benchmarks
- **Confusing layout**: Related metrics were scattered across different sections, breaking natural data relationships

#### Detailed Breakdown of Bad Practices

1. **Cluttered Metrics**
   > **Figure (add screenshot or diagram):** Dashboard panel showing 20+ numeric tiles in a grid with no size or color hierarchy — all metrics look equally important, forcing the viewer to scan everything.
- Too many metrics shown at once
   - No clear prioritization
   - Difficult to scan and understand

2. **Inconsistent Colors**
   > **Figure (add screenshot or diagram):** A bar chart where each bar has a different random color with no semantic meaning — some categories in red (but not negative), others in green (but not positive), creating visual noise.
- Random color choices
   - No consistent meaning
   - Hard to interpret quickly

3. **Poor Hierarchy**
   > **Figure (add screenshot or diagram):** Dashboard section where KPIs, secondary metrics, and footnotes all use the same font size and weight — nothing stands out as the most important number, making it impossible to prioritize at a glance.
- All elements given equal importance
   - No visual cues for prioritization
   - Confusing information architecture

### The Good Version

> **Figure (add screenshot or diagram):** A clean store analytics dashboard with 5 prominently placed KPI cards (Daily Sales, Units Sold, Customer Count, Avg. Basket, Return Rate), a sparkline trend, green/red indicators for each metric vs prior week, and a clear hierarchy guiding the eye top-to-bottom.

**Improvements Explained:**

- **Focused on key metrics**: Reduced to 5-7 critical KPIs that directly impact store performance
- **Clear visual hierarchy**: Used size, position, and color to guide attention to most important metrics
- **Consistent color scheme**: Green for positive trends, red for negative, blue for neutral
- **Added context and comparisons**: Included year-over-year changes and store performance rankings
- **Logical layout flow**: Grouped related metrics together (sales, inventory, customer satisfaction)

#### Detailed Breakdown of Good Practices

1. **Focused Metrics**
   > **Figure (add screenshot or diagram):** Three large KPI cards (Daily Sales, Customer Count, Avg. Basket) occupying the top row of the dashboard — each with a bold number, a small ↑/↓ trend arrow, and a sparkline; concise and scannable.
- Clear key performance indicators
   - Easy to scan and understand
   - Prioritized information

2. **Consistent Colors**
   > **Figure (add screenshot or diagram):** Same bar chart using a consistent semantic color scheme: green for categories above target, red for below target, and neutral gray for on-target — color carries meaning rather than just decoration.
- Meaningful color scheme
   - Consistent visual language
   - Clear data interpretation

3. **Clear Hierarchy**
   > **Figure (add screenshot or diagram):** Dashboard with clear visual hierarchy: primary KPIs in large bold text at the top (48px), secondary metrics in medium text in the middle (24px), and supporting detail tables in small text at the bottom (12px) — size signals importance.
- Visual importance levels
   - Clear information structure
   - Guided attention flow

### Key Learnings

1. **Focus on What Matters**
   - **Show only the most important metrics**: Walmart found that store managers made better decisions when presented with fewer, more relevant metrics
   - **Use size and position to indicate importance**: Critical metrics like daily sales and customer count were placed prominently
   - **Add context for better understanding**: Including store rankings helped managers understand their relative performance

2. **Use Color Purposefully**
   - **Red for negative trends**: Helped quickly identify underperforming categories
   - **Green for positive trends**: Made it easy to spot successful initiatives
   - **Neutral colors for context**: Used grays and blues for supporting information

3. **Create Clear Hierarchy**
   - **Most important metrics at the top**: Daily sales and customer count were always visible
   - **Supporting information below**: Detailed breakdowns were available but not distracting
   - **Details available on demand**: Additional metrics could be accessed through drill-downs

## Case Study 2: Customer Journey Analysis - Spotify's User Onboarding

### The Challenge

Spotify needed to understand why users were dropping off during the onboarding process. Their initial analysis showed a 40% drop-off rate between signup and first playlist creation.

### The Bad Version

> **Figure (add screenshot or diagram):** A text-heavy Spotify onboarding analysis document — dense paragraphs of prose with no visual flow diagram, no drop-off rate numbers called out, and no color coding to identify problem stages.

**Problems Explained:**

- **Text-heavy explanation**: Long paragraphs of text made it difficult to understand the flow
- **No visual flow**: Missing visual representation of the user journey
- **Missing key metrics**: Critical drop-off points weren't clearly identified
- **Hard to identify bottlenecks**: Couldn't quickly spot where users were getting stuck
- **No clear recommendations**: Analysis didn't lead to actionable insights

#### Detailed Breakdown of Bad Practices

1. **Text-Heavy Explanation**
   > **Figure (add screenshot or diagram):** A slide with five paragraphs of text and no charts — viewers must read every word to find that step 3 has a 40% drop-off rate, buried in the middle of a paragraph.
- Too much text
   - Hard to scan
   - Missing visual elements

2. **Missing Metrics**
   > **Figure (add screenshot or diagram):** Funnel chart with no percentage labels on the steps — bars get smaller from top to bottom but the viewer cannot tell if the drop-off is 5% or 40% at each stage without reading footnotes.
- No clear data points
   - Missing key indicators
   - Hard to measure success

3. **No Flow**
   > **Figure (add screenshot or diagram):** Bullet list of onboarding steps (Sign Up, Verify Email, Choose Plan, Create Playlist) with no connecting arrows or visual progression — steps appear as disconnected items rather than a sequential journey.
- Disconnected steps
   - No clear progression
   - Hard to follow journey

### The Good Version

> **Figure (add screenshot or diagram):** A Spotify onboarding funnel diagram with 5 sequential steps (Sign Up → Verify → Choose Plan → Follow Artists → Create Playlist), each step showing a completion percentage, color-coded green (>80%), yellow (50-80%), and red (<50%) for the critical "Create Playlist" step where 40% drop-off is highlighted with a callout annotation.

**Improvements Explained:**

- **Visual flow diagram**: Created a clear path showing each step of the onboarding process
- **Color-coded stages**: Used colors to indicate success (green), warning (yellow), and critical (red) stages
- **Clear metrics at each step**: Added conversion rates and drop-off percentages
- **Highlighted pain points**: Clearly marked where users were abandoning the process
- **Actionable insights**: Included specific recommendations for each stage

#### Detailed Breakdown of Good Practices

1. **Visual Flow**
   > **Figure (add screenshot or diagram):** Flow diagram with step boxes connected by horizontal arrows — each box has an icon (email ✉, checkmark ✓, music note ♪) and a conversion rate below it; the journey is scannable left-to-right in seconds.
- Clear progression
   - Visual connections
   - Easy to follow

2. **Clear Metrics**
   > **Figure (add screenshot or diagram):** Each onboarding step box annotated with: total users entering (top), users completing (middle), and drop-off rate in bold red below — key numbers visible without needing to look them up.
- Key data points
   - Drop-off rates
   - Success metrics

3. **Actionable Insights**
   > **Figure (add screenshot or diagram):** A callout box beside the worst-performing step (Create Playlist, 40% drop-off) listing three specific recommendations: "Add auto-generated starter playlist", "Reduce required fields", "Send reminder email at 24h" — insights tied directly to the data.
- Critical points
   - Improvement areas
   - Clear recommendations

### Key Learnings

1. **Make It Visual**
   - **Use flow diagrams**: Spotify's team found that visual journey maps were 3x more effective at communicating insights
   - **Add icons and symbols**: Used intuitive icons to represent different stages
   - **Create visual hierarchy**: Made critical stages stand out through size and color

2. **Show the Data**
   - **Include key metrics**: Added conversion rates, time spent, and drop-off percentages
   - **Use color for emphasis**: Red highlighted critical drop-off points
   - **Add comparisons**: Showed how metrics compared to industry benchmarks

3. **Drive Action**
   - **Highlight problems**: Clearly identified where users were getting stuck
   - **Suggest solutions**: Provided specific recommendations for each stage
   - **Show impact**: Estimated the potential improvement from each change

## Case Study 3: Marketing Campaign Analysis - Airbnb's Growth Strategy

### The Challenge

Airbnb needed to report on the performance of their latest marketing campaign across different channels to optimize their $1.2B marketing budget.

### The Bad Version

> **Figure (add screenshot or diagram):** An Airbnb marketing report showing a raw data table — 8 columns (Channel, Impressions, Clicks, CTR, CPA, Spend, Conversions, ROAS) with 20 rows of numbers and no charts, no color coding, and no highlighted winners — the "before" illustrating data dump without story.

**Problems Explained:**

- **Raw data dump**: Presented all metrics without filtering or prioritization
- **No clear story**: Failed to connect the data to business objectives
- **Missing context**: Lacked comparison to previous campaigns and industry benchmarks
- **Hard to compare channels**: Different metrics made it difficult to evaluate channel performance
- **No actionable insights**: Data didn't lead to clear recommendations

#### Detailed Breakdown of Bad Practices

1. **Raw Data Dump**
   > **Figure (add screenshot or diagram):** A dense numeric table with no sorting, no color, and no highlights — all channels and all metrics presented in the same visual weight, forcing the reader to scan every cell to find the best-performing channel.
- Unprocessed data
   - No filtering
   - Hard to interpret

2. **No Story**
   > **Figure (add screenshot or diagram):** A slide with the title "Q3 Marketing Results" and a bar chart showing impressions by channel — but no mention of which channel drove the most revenue, no link to the campaign objective, and no next-step recommendation.
- Missing narrative
   - No clear message
   - Hard to understand

3. **Missing Context**
   > **Figure (add screenshot or diagram):** Channel performance table with ROAS values but no prior-period comparison — a 2.3x ROAS shown with no indication of whether that is good, bad, or typical for the industry.
- No comparisons
   - No benchmarks
   - Hard to evaluate

### The Good Version

> **Figure (add screenshot or diagram):** An Airbnb campaign performance report with a narrative headline ("Paid Search delivered 4x ROAS, outperforming Social by 60%"), a channel comparison bar chart using consistent ROAS metric, YoY change annotations, and a recommendation box at the bottom suggesting budget reallocation toward Search.
**Improvements Explained:**

- **Clear narrative structure**: Started with objectives, showed results, ended with recommendations
- **Channel comparisons**: Used consistent metrics to compare performance across channels
- **Performance metrics**: Focused on ROI and customer acquisition cost
- **ROI calculations**: Showed return on investment for each channel
- **Actionable recommendations**: Provided specific budget allocation suggestions

#### Detailed Breakdown of Good Practices

1. **Clear Narrative**
   > **Figure (add screenshot or diagram):** Report layout showing three sections labelled "Objective", "Results", and "Recommendations" with a clear visual divider between each — the reader knows exactly where to find the story, the evidence, and the action.
- Story structure
   - Clear progression
   - Logical flow

2. **Channel Comparisons**
   > **Figure (add screenshot or diagram):** Horizontal bar chart of ROAS by channel (Paid Search, Social, Email, Display, Affiliate) sorted descending — all using the same metric on a single shared scale, making relative performance instantly comparable.
- Consistent metrics
   - Easy comparison
   - Clear differences

3. **ROI Focus**
   > **Figure (add screenshot or diagram):** Summary scorecard showing ROI and Customer Acquisition Cost (CAC) for each channel — two KPI columns per row with color indicators (green if above target, red if below), putting the business-critical metrics front and center.
- Key metrics
   - Performance indicators
   - Clear outcomes

### Key Learnings

1. **Tell a Story**
   - **Start with context**: Explained campaign objectives and target audience
   - **Show the journey**: Presented how different channels contributed to overall success
   - **End with insights**: Concluded with clear recommendations

2. **Make Comparisons Easy**
   - **Use consistent metrics**: Standardized on ROI and customer acquisition cost
   - **Add benchmarks**: Compared performance to industry standards
   - **Show trends**: Included historical performance for context

3. **Focus on Impact**
   - **Show ROI**: Highlighted return on investment for each channel
   - **Highlight successes**: Emphasized channels that exceeded expectations
   - **Identify opportunities**: Pointed out areas for potential improvement

## Case Study 4: Financial Performance Report - Tesla's Quarterly Results

### The Challenge

Tesla's finance team needed to present quarterly results to the board of directors, explaining complex financial data in a clear and compelling way.

### The Bad Version

> **Figure (add screenshot or diagram):** A Tesla quarterly board deck slide showing a 10-column table of raw financial data — Revenue, COGS, Gross Profit, R&D, SG&A, EBIT, Net Income, EPS, FCF, Capex — for 8 quarters in small gray font with no charts or highlights; the "before" version overwhelming any audience.

**Problems Explained:**

- **Too many numbers**: Overwhelmed audience with raw financial data
- **No visual aids**: Relied solely on tables and text
- **Missing context**: Failed to explain the significance of the numbers
- **Hard to understand trends**: Made it difficult to see performance patterns
- **No clear message**: Didn't highlight key achievements or challenges

#### Detailed Breakdown of Bad Practices

1. **Too Many Numbers**
   > **Figure (add screenshot or diagram):** Quarterly P&L table with 10 rows × 8 quarters = 80 cells of numbers in size-10 font — no shading, no totals highlighted, and no visual cue for which quarter is current; pure data overload.
- Data overload
   - No filtering
   - Hard to process

2. **No Visual Aids**
   > **Figure (add screenshot or diagram):** A text-only slide with four bullet points describing revenue changes ("Revenue grew 12% YoY… up from $19.3B… margin improved 0.4pp…") — trends that a simple line chart would communicate instantly are buried in prose.
- Missing charts
   - Text-heavy
   - Hard to visualize

3. **Missing Context**
   > **Figure (add screenshot or diagram):** A net income figure "$1.1B" shown in isolation with no YoY comparison, no analyst consensus, and no prior quarter — the reader cannot tell if this is a beat, a miss, or a new record.
- No comparisons
   - No benchmarks
   - Hard to evaluate

### The Good Version

> **Figure (add screenshot or diagram):** Tesla board presentation slide: three KPI cards at the top (Revenue $24B ↑12% YoY, Gross Margin 18.2% ↑0.4pp, FCF $2.1B), a 8-quarter revenue trend line below with the current quarter highlighted, and a single annotation "Record automotive deliveries drove Q3 outperformance."
**Improvements Explained:**

- **Key metrics highlighted**: Focused on revenue growth, profit margins, and cash flow
- **Visual trends**: Used line charts to show performance over time
- **Year-over-year comparisons**: Added context through historical data
- **Clear narrative**: Connected financial results to business strategy
- **Actionable insights**: Provided clear next steps and recommendations

#### Detailed Breakdown of Good Practices

1. **Key Metrics**
   > **Figure (add screenshot or diagram):** Three large KPI cards displaying Revenue, Gross Margin, and Free Cash Flow — each with a bold current-quarter value, a smaller YoY delta in green/red, and a sparkline for the past 4 quarters.
- Focused indicators
   - Clear trends
   - Important data

2. **Visual Trends**
   > **Figure (add screenshot or diagram):** Line chart of 8 quarters of revenue with a shaded area between the trend line and the baseline, the current quarter's point highlighted with a callout label, and a dotted forecast line extending 2 quarters ahead.
- Clear patterns
   - Easy to follow
   - Time-based view

3. **Year-over-Year**
   > **Figure (add screenshot or diagram):** Grouped bar chart comparing Q3 performance across the same quarter for 3 years (2022, 2023, 2024) side by side — each group has 3 bars in the same color family with shading, making YoY growth immediately visible.
- Historical context
   - Clear comparisons
   - Progress tracking

### Key Learnings

1. **Simplify Complex Data**
   - **Use charts and graphs**: Made trends and patterns immediately visible
   - **Highlight key numbers**: Emphasized the most important metrics
   - **Add context**: Explained what the numbers meant for the business

2. **Show Trends**
   - **Use line charts**: Made it easy to see performance over time
   - **Add comparisons**: Showed how current results compared to previous periods
   - **Show progress**: Highlighted improvements and areas of concern

3. **Make It Actionable**
   - **Clear recommendations**: Provided specific next steps
   - **Impact analysis**: Showed the potential impact of different decisions
   - **Next steps**: Outlined immediate actions needed

## Case Study 5: Product Usage Analytics - Netflix's Content Strategy

### The Challenge

Netflix needed to understand how users were interacting with their platform to optimize content recommendations and improve user engagement.

### The Bad Version

> **Figure (add screenshot or diagram):** A Netflix internal analytics report showing a raw CSV-style table — 15 columns including feature_id, session_count, avg_duration_sec, p50_engagement, p95_engagement — with no charts, no feature names, and no indication of which features matter most.

**Problems Explained:**

- **Raw data tables**: Presented unprocessed usage statistics
- **No visualizations**: Failed to show patterns and trends
- **Missing patterns**: Couldn't identify user behavior patterns
- **Hard to identify issues**: Made it difficult to spot engagement problems
- **No clear insights**: Data didn't lead to actionable recommendations

#### Detailed Breakdown of Bad Practices

1. **Raw Data Tables**
   > **Figure (add screenshot or diagram):** A spreadsheet grid of 200 rows × 12 columns of usage event data — timestamps, session IDs, feature codes — with no aggregation or summarization; the analyst must write queries just to get any insight.
- Unprocessed data
   - No filtering
   - Hard to interpret

2. **No Visualizations**
   > **Figure (add screenshot or diagram):** A slide titled "Feature Engagement Report" containing only a numbered list of feature names and session counts — no bar chart, no trend line, no color differentiation; features that differ by 10× in usage look identical in the list.
- Missing charts
   - Text-heavy
   - Hard to visualize

3. **Missing Patterns**
   > **Figure (add screenshot or diagram):** A line chart of daily active users with no seasonality annotation — the weekly dip on weekends is visible but unlabeled, leaving the viewer to wonder if the drop is a bug or expected behavior.
- No trends
   - No connections
   - Hard to analyze

### The Good Version

> **Figure (add screenshot or diagram):** A Netflix usage analytics dashboard with a Sankey/flow diagram showing the most common viewing paths (Browse → Search → Play, or Browse → Play Directly), a feature usage bar chart sorted by engagement with the top 5 highlighted in teal, and a heatmap of hourly usage by day of week showing peak engagement patterns.

**Improvements Explained:**

- **User flow diagrams**: Showed how users navigated through the platform
- **Feature usage charts**: Highlighted most and least used features
- **Time-based patterns**: Revealed when and how users engaged with content
- **Clear insights**: Identified key opportunities for improvement
- **Actionable recommendations**: Provided specific suggestions for enhancing engagement

#### Detailed Breakdown of Good Practices

1. **User Flow**
   > **Figure (add screenshot or diagram):** Sankey diagram of Netflix user navigation flows — nodes for Home, Search, Browse, Play, and Exit; arrow widths proportional to the number of users taking each path; the Home → Play direct path shown as the widest arrow.
- Clear paths
   - User journeys
   - Navigation patterns

2. **Feature Usage**
   > **Figure (add screenshot or diagram):** Horizontal bar chart of Netflix features ranked by weekly active users — Search, Continue Watching, Top 10, My List, Downloads — with the top 3 bars highlighted in teal and the bottom 2 in gray, immediately signaling where to invest vs deprioritize.
- Popular features
   - Usage patterns
   - Engagement levels

3. **Time Patterns**
   > **Figure (add screenshot or diagram):** Heatmap of Netflix streaming sessions by hour of day (y-axis, 0–23) and day of week (x-axis, Mon–Sun) — darker cells for high-engagement times revealing the Friday and Saturday evening peak cluster around 8–10 PM.
- Usage trends
   - Time-based analysis
   - Behavioral patterns

### Key Learnings

1. **Visualize User Behavior**
   - **Use flow diagrams**: Showed how users moved through the platform
   - **Show patterns**: Revealed common user journeys
   - **Highlight trends**: Identified changing user preferences

2. **Make It Actionable**
   - **Identify issues**: Pinpointed where users were getting stuck
   - **Suggest improvements**: Provided specific recommendations
   - **Show impact**: Estimated the potential improvement from changes

3. **Focus on Insights**
   - **Clear findings**: Highlighted key discoveries
   - **Supporting data**: Provided evidence for recommendations
   - **Next steps**: Outlined immediate actions needed

## Common Themes Across Case Studies

### 1. The Power of Focus

- **Show only what matters**: Each company found that focusing on key metrics led to better decisions
- **Create clear hierarchy**: Using visual hierarchy helped guide attention to important information
- **Guide the audience**: Clear storytelling helped stakeholders understand and act on insights

### 2. The Importance of Context

- **Add benchmarks**: Companies like Walmart and Tesla used industry benchmarks to provide context
- **Show comparisons**: Spotify and Netflix used historical data to show trends
- **Provide background**: Airbnb and others explained the business context for their data

### 3. The Need for Action

- **Clear insights**: Each company focused on actionable insights rather than just data
- **Specific recommendations**: Provided concrete next steps for improvement
- **Measurable impact**: Showed the potential impact of recommended changes

## How to Apply These Lessons

### 1. Start with Your Audience

- **What do they need to know?**: Understand your audience's key concerns and questions
- **What decisions do they need to make?**: Focus on data that supports decision-making
- **How can you help them?**: Provide clear, actionable insights

### 2. Focus on the Story

- **What's the main message?**: Identify the key takeaway
- **What evidence supports it?**: Use data to back up your story
- **What should happen next?**: Provide clear next steps

### 3. Make It Visual

- **Choose the right charts**: Select visualizations that best represent your data
- **Use color purposefully**: Use color to highlight important information
- **Create clear hierarchy**: Guide your audience through the information

### 4. Drive Action

- **Clear recommendations**: Provide specific, actionable suggestions
- **Measurable impact**: Show the potential results of your recommendations
- **Next steps**: Outline immediate actions needed

## Practice Exercise: Analyze Your Own Work

### Step 1: Review Your Current Work

- **What's working well?**: Identify successful elements
- **What could be improved?**: Look for areas of confusion or clutter
- **What's missing?**: Consider what additional context or insights would help

### Step 2: Apply the Lessons

- **Focus on key messages**: Reduce to the most important points
- **Add visual elements**: Use charts and diagrams to illustrate key points
- **Create clear hierarchy**: Guide your audience through the information

### Step 3: Get Feedback

- **Show to colleagues**: Get input from different perspectives
- **Ask specific questions**: Focus on clarity and actionability
- **Iterate and improve**: Use feedback to refine your work

## Gotchas

- **Reducing to "5-7 critical KPIs" only works if you've agreed on which ones matter** — the Walmart case shows a clean dashboard with five KPIs, but choosing the wrong five is worse than showing more. Consult the decision-maker before cutting metrics; stakeholders often have a "non-negotiable" KPI that looks secondary to an analyst.
- **A funnel chart implies the same cohort flows through each step, which is often false** — in the Spotify case, the funnel shows absolute user counts per step. If different users enter at different steps (e.g., re-activation flows), the funnel overstates drop-off. Label whether it is a cohort funnel or a cross-sectional snapshot.
- **Comparing channels on a single metric like ROAS hides the volume-efficiency trade-off** — the Airbnb case addresses this with the "ROI Focus" improvement, but a single ROAS bar chart can make a small high-ROAS channel look better than a large moderate-ROAS channel even when the latter generates more absolute profit. Show both dimensions or be explicit about what you're optimising.
- **Using "record X drove Y outcome" language on a board deck implies causation without a control** — the Tesla case frames quarterly results against prior periods, which is appropriate, but learners often copy this pattern into their own analyses and present correlation as causation. Always hedge with "consistent with" or "coinciding with" unless you have an experiment.
- **Flow diagrams like the Netflix Sankey become misleading if path widths aren't proportional to the same unit** — if "Browse → Play" width encodes unique users but "Browse → Search" width encodes sessions, the chart looks comparable but isn't. Ensure a single consistent unit (users, sessions, or events) drives all path widths before publishing.

Remember: The best data stories are those that make complex information simple and actionable. Use these case studies as inspiration, but adapt the lessons to your specific needs and audience.
