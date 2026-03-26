# Getting Started with Google Colab

## What is Google Colab?

Google Colab (short for Colaboratory) is a **free** online platform that lets you write and run Python code directly in your web browser - no installation needed!

**In simple terms:** Think of it as Jupyter Notebooks that run in the cloud. You can write code, see results, and even use powerful GPUs (graphics cards) for free - perfect for machine learning!

**Why use Colab?**
- ✅ **Free** - No cost, no credit card needed
- ✅ **No setup** - Works in any web browser
- ✅ **Free GPUs** - Access to powerful processors for machine learning
- ✅ **Pre-installed libraries** - Popular data science tools ready to use
- ✅ **Easy sharing** - Share notebooks with others instantly
- ✅ **Saves to Google Drive** - Your work is automatically backed up

> **Figure (add screenshot or diagram):** Colab notebook with code cell and output.

## System Requirements

- Modern web browser (Chrome recommended)
- Google account
- Stable internet connection
- No local installation required

## Key Features

- Free access to GPUs and TPUs
- Pre-installed data science libraries
- Integration with Google Drive
- Real-time collaboration
- Markdown and code cells
- File upload/download capabilities
- GitHub integration

## Account Setup

> **Time needed:** Less than 2 minutes!

**Step 1: Sign In**
1. Visit [Google Colab](https://colab.research.google.com)
2. Click **"Sign in"** in the top right corner
3. Use your Google account (Gmail account works perfectly!)
4. Accept the terms of service if prompted

> **Figure (add screenshot or diagram):** Colab welcome / sign-in page.

**Step 2: Create Your First Notebook**
- Click **"File"** → **"New notebook"**, OR
- Click the **"+ New Notebook"** button on the welcome page

That's it! You're ready to start coding.

> **Tip:** If you see example notebooks on the welcome page, feel free to explore them - they're great learning resources!

## Initial Configuration

### Creating a New Notebook

**Method 1:** Click **"File"** → **"New notebook"** in the menu bar
**Method 2:** Click the **"+ New Notebook"** button on the welcome page

> **Figure (add screenshot or diagram):** Welcome screen with **New notebook** or **File → New notebook**.

### Basic Setup

**Step 1: Rename Your Notebook**
1. Click on **"Untitled0.ipynb"** at the top of the page
2. Type a descriptive name (e.g., "Data Analysis Project")
3. Press Enter

**Step 2: Configure Runtime (Optional but Recommended)**

The runtime is the "computer" that runs your code. You can choose to use a GPU for faster machine learning!

1. Click **"Runtime"** in the menu bar
2. Select **"Change runtime type"**
3. In the popup:
   - **Hardware accelerator:** Choose "GPU" if you're doing machine learning (free tier available!)
   - **Runtime shape:** Leave as default
4. Click **"Save"**

> **Figure (add screenshot or diagram):** **Runtime → Change runtime type** dialog (GPU/TPU options).

> **Note:** GPU access is free but limited. If you get a message saying GPUs aren't available, you can still use Colab - just select "None" for the hardware accelerator.

### Mounting Google Drive

Want to access files from your Google Drive? Mount it with this simple code:

```python
# Run this in a code cell
from google.colab import drive
drive.mount('/content/drive')
```

**What happens:**
1. A popup will ask for permission - click **"Allow"**
2. Copy the authorization code that appears
3. Paste it into the input box in Colab
4. Your Google Drive is now accessible at **/content/drive/MyDrive/**

> **Figure (add screenshot or diagram):** Google Drive mount authorization step.

> **Tip:** After mounting, you can load files with Pandas, for example paths under **/content/drive/MyDrive/**.

## Best Practices

### Resource Management

1. **Runtime Management**:
   - Use **Runtime → Disconnect and delete runtime** when done
   - Be aware of **idle disconnects** (free tier limits change over time; see the [Colab FAQ](https://research.google.com/colaboratory/faq.html))
   - Save work frequently

2. **Storage**:
   - Keep notebooks in Google Drive
   - Use `/content` for temporary files (this storage is cleared when the runtime is recycled)
   - Download important results

### Code Organization

1. **Cell Structure**:
   - Use markdown cells for documentation
   - Keep code cells focused and modular
   - Include cell outputs in saved notebooks

2. **Package Management**:
   ```python
   # Install additional packages
   %pip install package_name
   ```
   After installing packages that affect imports, use **Runtime → Restart runtime** so notebooks pick up the new libraries.

## Common Issues & Troubleshooting

### Connection Problems

1. **Runtime Disconnects**:
   - Check internet connection
   - Reduce idle time
   - Save work frequently
   - Reconnect manually

2. **Resource Limits**:
   - Monitor RAM usage
   - Clear output cells
   - Restart runtime
   - Use smaller datasets

### Performance Issues

1. **Slow Execution**:
   - Check resource usage
   - Clear unnecessary outputs
   - Optimize code
   - Consider GPU runtime

2. **Memory Errors**:
   - Reduce data size
   - Use batch processing
   - Clear variables
   - Restart runtime

## Tips for Success

1. **Keyboard Shortcuts**:
   - **Ctrl+Enter**: Run cell
   - **Shift+Enter**: Run cell and select below
   - **Alt+Enter**: Run cell and insert below
   - **Ctrl+M B**: Insert cell below
   - **Ctrl+M A**: Insert cell above
   - **Ctrl+M D**: Delete cell

2. **File Management**:
   ```python
   # Upload files
   from google.colab import files
   uploaded = files.upload()
   
   # Download files
   files.download('filename.ext')
   ```

3. **Collaboration**:
   - Share notebooks via link
   - Control access permissions
   - Use comments for feedback
   - Enable real-time collaboration

## Additional Resources

1. **Documentation**:
   - [Colab Overview](https://colab.research.google.com/notebooks/basic_features_overview.ipynb)
   - [Colab Pro Features](https://colab.research.google.com/signup)
   - [FAQ](https://research.google.com/colaboratory/faq.html)

2. **Learning Materials**:
   - [Example Notebooks](https://colab.research.google.com/notebooks/welcome.ipynb)
   - [Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course)
   - [TensorFlow Tutorials](https://www.tensorflow.org/tutorials)

3. **Community Support**:
   - [Stack Overflow](https://stackoverflow.com/questions/tagged/google-colab)
   - [GitHub Issues](https://github.com/googlecolab/colabtools/issues)
   - [Google Groups](https://groups.google.com/forum/#!forum/colaboratory)
