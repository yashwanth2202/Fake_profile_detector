import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
def generate_report():
    # Target path is d:\fake_profile_detector\draft_report_ultimate.pdf
    pdf_path = os.path.join("d:\\fake_profile_detector", "draft_report_ultimate.pdf")
    
    # Page setup
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        rightMargin=54,
        leftMargin=54,
        topMargin=54,
        bottomMargin=54
    )
    
    styles = getSampleStyleSheet()
    
    # Custom Palette
    primary_color = colors.HexColor("#1A365D")   # Dark Navy
    secondary_color = colors.HexColor("#2B6CB0") # Medium Blue
    accent_color = colors.HexColor("#2F855A")    # Green
    text_color = colors.HexColor("#2D3748")      # Slate Gray
    bg_light = colors.HexColor("#F7FAFC")        # Off-white
    border_color = colors.HexColor("#E2E8F0")    # Light Gray
    
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=22,
        leading=26,
        textColor=primary_color,
        spaceAfter=6
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=11,
        leading=14,
        textColor=secondary_color,
        spaceAfter=15
    )
    
    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=17,
        textColor=primary_color,
        spaceBefore=12,
        spaceAfter=6,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'Heading2_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=13,
        textColor=secondary_color,
        spaceBefore=10,
        spaceAfter=5,
        keepWithNext=True
    )
    
    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=text_color,
        spaceAfter=6
    )
    
    bullet_style = ParagraphStyle(
        'Bullet_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=12.5,
        textColor=text_color,
        leftIndent=15,
        firstLineIndent=-10,
        spaceAfter=4
    )
    
    code_style = ParagraphStyle(
        'Code_Custom',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=7.5,
        leading=10,
        textColor=colors.HexColor("#1A202C"),
        backColor=bg_light,
        borderColor=border_color,
        borderWidth=1,
        borderPadding=6,
        spaceAfter=8
    )
    
    table_header_style = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=9.5,
        textColor=colors.white
    )
    
    table_cell_style = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=10,
        textColor=text_color
    )

    table_cell_bold_style = ParagraphStyle(
        'TableCellBold',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        textColor=text_color
    )

    callout_style = ParagraphStyle(
        'Callout_Style',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=8.5,
        leading=12.5,
        textColor=colors.HexColor("#2C5282"),
        backColor=colors.HexColor("#EBF8FF"),
        borderColor=colors.HexColor("#BEE3F8"),
        borderWidth=1,
        borderPadding=8,
        spaceBefore=4,
        spaceAfter=6
    )
    
    story = []
    
    # Title & Subtitle
    story.append(Paragraph("Comprehensive Project Execution Report: Fake Profile Detector", title_style))
    story.append(Paragraph("AI-Powered Fake Profile Detector — Step-by-Step Execution Draft", subtitle_style))
    story.append(Spacer(1, 4))
    
    # Executive Summary
    story.append(Paragraph("Executive Summary", h2_style))
    story.append(Paragraph(
        "Social media platforms are increasingly plagued by automated bots and malicious fake profiles. "
        "These accounts are often used for identity theft, spamming, spreading disinformation, and inflating "
        "social engagement metrics. <b>Fake Profile Detector</b> addresses this issue by leveraging supervised machine learning "
        "to classify accounts into two categories: <b>Real</b> (Class 0) or <b>Fake</b> (Class 1). "
        "By analyzing public metadata like follower counts, posting activity, name formatting, and bio content, "
        "Fake Profile Detector provides a local web-based inference engine that predicts profile authenticity with "
        "<b>90.52% accuracy</b>. This report compiles the comprehensive lifecycle of the project, including scope "
        "definition, system design, implementation hurdles, performance metrics, and validation test cases.",
        body_style
    ))
    story.append(Spacer(1, 4))
    
    # STEP 1
    story.append(Paragraph("Step 1: Define Scope & Requirements", h1_style))
    story.append(Paragraph("<b>1. Project Objectives:</b>", body_style))
    story.append(Paragraph("• <b>High Accuracy Classification:</b> Target a prediction accuracy of <b>>90%</b> on unseen test data using supervised machine learning.", bullet_style))
    story.append(Paragraph("• <b>Sub-Second Web Inference:</b> Provide a responsive Flask web interface that executes predictions and returns verdicts in less than 100 milliseconds.", bullet_style))
    story.append(Paragraph("• <b>Privacy-First Design:</b> Build the detector entirely around publicly observable profile metrics (follower counts, post counts, bio characteristics) rather than scraping private user data or media content.", bullet_style))
    story.append(Paragraph("• <b>Developer-Friendly Extensibility:</b> Organize the codebase into modular pipelines so new features, data sources, and models can be easily integrated.", bullet_style))
    
    story.append(Paragraph("<b>2. Core Features:</b>", body_style))
    story.append(Paragraph("• <b>Offline Training & Evaluation Pipeline:</b> A set of structured Python modules to ingest raw CSV data, perform feature engineering, split datasets into training and validation sets, train a classifier, and output detailed validation metrics.", bullet_style))
    story.append(Paragraph("• <b>Dynamic Feature Engineering:</b> Automate the extraction of advanced behavioral signals, such as follower-to-following ratios and posts-to-following ratios, which highlight anomalous user behavior.", bullet_style))
    story.append(Paragraph("• <b>Web Interface (Fake Profile Detector Dashboard):</b> An interactive, responsive, and visually appealing web interface built using HTML5, CSS3, and JavaScript, featuring glassmorphism elements, loading animations, and dynamic result styling.", bullet_style))
    story.append(Paragraph("• <b>Serialized Model Inference Layer:</b> A lightweight server-side inference module that loads a pre-trained model file (<i>model.pkl</i>) into memory when Flask starts up to process and classify incoming JSON payloads.", bullet_style))
    
    story.append(Paragraph("<b>3. Constraints & Dependencies:</b>", body_style))
    story.append(Paragraph("• <b>Rate Limiting & Anti-Scraping:</b> Instagram employs aggressive anti-scraping measures that can block IP addresses or request accounts to solve Captchas. To ensure 100% availability and prevent blocks, Fake Profile Detector operates strictly on user-supplied parameters rather than automated backend scraping.", bullet_style))
    story.append(Paragraph("• <b>Data Completeness:</b> The accuracy of predictions depends on the presence of public metadata. Profiles that hide their metrics or are completely locked down can limit the input space.", bullet_style))
    story.append(Paragraph("• <b>Technical Stack:</b> Python 3.x, Pandas & NumPy (data loading & arrays), Scikit-Learn (preprocessing & splitting), XGBoost (ensemble classification trees), and Flask (backend serving layout).", bullet_style))
    
    story.append(PageBreak())

    # STEP 2
    story.append(Paragraph("Step 2: System Design & Methodology", h1_style))
    story.append(Paragraph(
        "The system architecture separates the heavy computational training process from the lightweight serving layer. "
        "This division ensures that the production web server remains fast and responsive. The lifecycle flow is detailed below:",
        body_style
    ))
    
    # Architecture Table
    arch_data = [
        [
            Paragraph("Phase / File", table_header_style), 
            Paragraph("Stage", table_header_style), 
            Paragraph("Description & Data Flow", table_header_style)
        ],
        [Paragraph("<b>Offline:</b> dataset.csv", table_cell_style), Paragraph("Data Source", table_cell_style), Paragraph("Contains raw profile stats of 576 accounts.", table_cell_style)],
        [Paragraph("<b>Offline:</b> data_loader.py", table_cell_style), Paragraph("Ingestion", table_cell_style), Paragraph("Loads raw CSV into Pandas DataFrame.", table_cell_style)],
        [Paragraph("<b>Offline:</b> feature_engineer.py", table_cell_style), Paragraph("Feature Prep", table_cell_style), Paragraph("Calculates follower ratios & bio boolean indicators.", table_cell_style)],
        [Paragraph("<b>Offline:</b> preprocessor.py", table_cell_style), Paragraph("Splitting", table_cell_style), Paragraph("Separates target class and splits 80% train / 20% test.", table_cell_style)],
        [Paragraph("<b>Offline:</b> model_trainer.py", table_cell_style), Paragraph("Training", table_cell_style), Paragraph("Trains XGBoost Classifier and saves model.pkl to disk.", table_cell_style)],
        [Paragraph("<b>Offline:</b> visualiser.py", table_cell_style), Paragraph("Evaluation", table_cell_style), Paragraph("Runs predictions on test set and outputs accuracy.", table_cell_style)],
        [Paragraph("<b>Online:</b> app.py / Web UI", table_cell_style), Paragraph("Web Interface", table_cell_style), Paragraph("User inputs stats on dashboard; receives instant predictions.", table_cell_style)],
        [Paragraph("<b>Online:</b> predictor.py", table_cell_style), Paragraph("Inference", table_cell_style), Paragraph("Loads model.pkl, executes feature ratios, predicts output class.", table_cell_style)]
    ]
    
    t_arch = Table(arch_data, colWidths=[110, 80, 310])
    t_arch.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), primary_color),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('BOTTOMPADDING', (0,0), (-1,0), 3),
        ('TOPPADDING', (0,0), (-1,0), 3),
        ('GRID', (0,0), (-1,-1), 0.5, border_color),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, bg_light]),
        ('TOPPADDING', (0,1), (-1,-1), 3),
        ('BOTTOMPADDING', (0,1), (-1,-1), 3),
    ]))
    story.append(t_arch)
    story.append(Spacer(1, 4))
    
    story.append(Paragraph("<b>Feature Engineering Theory:</b>", h2_style))
    story.append(Paragraph(
        "To expose anomalies typical of bot behavior, 4 specialized features are engineered:<br/>"
        "• <b>Follower-to-Following Ratio:</b> Real users typically establish mutual connections or follow a selective set of accounts, resulting in balanced ratios. In contrast, bot accounts mass-follow thousands of users to gain follow-backs while having very few followers of their own. Formula: <i>followers / (follows + 1)</i>. (The +1 smoothing term avoids division-by-zero).<br/>"
        "• <b>Posts-to-Following Ratio:</b> Flags inactive accounts that follow massive numbers of users. Formula: <i>posts / (follows + 1)</i>.<br/>"
        "• <b>Has Bio:</b> Boolean flag (1/0) indicating whether description length > 0. Automated bot creators often skip writing profile biographies to save creation time.<br/>"
        "• <b>Has Full Name:</b> Boolean flag (1/0) showing if full name words > 0.",
        body_style
    ))
    
    story.append(Paragraph("<b>Machine Learning Algorithm: XGBoost</b>", h2_style))
    story.append(Paragraph(
        "We chose <b>XGBoost (Extreme Gradient Boosting)</b> as our classification model. XGBoost builds an ensemble of weak decision trees sequentially, with each subsequent tree focusing on correcting the errors made by its predecessors. "
        "It is highly optimized for tabular datasets, handles missing values naturally, prevents overfitting via regularization parameters, and requires no feature scaling (unlike SVMs or neural networks).<br/>"
        "<b>Hyperparameter Settings:</b> <i>n_estimators = 100</i> (number of trees), <i>max_depth = 6</i> (limits depth to prevent overfitting), <i>learning_rate = 0.3</i> (step size shrinkage), and <i>eval_metric = 'logloss'</i>.",
        body_style
    ))
    
    story.append(PageBreak())
    
    # STEP 3
    story.append(Paragraph("Step 3: Development & Implementation (Engineering Logbook)", h1_style))
    story.append(Paragraph("<b>1. Codebase Layout & Script Walkthrough:</b>", body_style))
    
    structure_text = (
        "d:\\fake_profile_detector\\\n"
        "├── app.py                     # Flask web server and backend logic\n"
        "├── config.py                  # Hyperparameter configuration\n"
        "├── main.py                    # Master pipeline runner\n"
        "└── src/\n"
        "    ├── data_loader.py         # CSV file reader\n"
        "    ├── feature_engineer.py    # Automated ratio computations\n"
        "    ├── preprocessor.py        # Train/test set splitting\n"
        "    ├── model_trainer.py       # XGBoost classifier training\n"
        "    ├── visualiser.py          # Model evaluation reporting\n"
        "    └── predictor.py           # On-the-fly requests parser"
    )
    story.append(Paragraph(structure_text.replace("\n", "<br/>").replace(" ", "&nbsp;"), code_style))
    
    story.append(Paragraph("<b>2. Log of Development Hurdles & Bug Resolution:</b>", h2_style))
    story.append(Paragraph(
        "<b>Hurdle A (Division-by-Zero Exceptions):</b> Accounts with 0 following counts caused program crashes and "
        "produced NaN values during feature extraction. We resolved this by adding a +1 smoothing factor to the "
        "denominators: <i>df['follower_following_ratio'] = df['#followers'] / (df['#follows'] + 1)</i>. This guarantees continuous, "
        "valid numerical ranges across all users.",
        callout_style
    ))
    story.append(Paragraph(
        "<b>Hurdle B (Frontend-to-Model Feature Mapping):</b> Flask clients submit string fields (like biography, username, "
        "fullname), but the XGBoost model expects numeric metrics. To bridge this gap without scraping backend endpoints, we "
        "built string-to-numeric converters in <i>app.py</i> that dynamically compute digit-ratios, word counts, and bio lengths "
        "on incoming requests.",
        callout_style
    ))
    story.append(Paragraph(
        "<b>Hurdle C (Robust Input Type Parsing):</b> Users leaving input fields blank or entering invalid non-numeric strings "
        "originally triggered Flask internal server errors. We resolved this by writing a <i>safe_int()</i> wrapper inside "
        "<i>app.py</i> that catches TypeErrors and ValueErrors, defaulting empty strings or invalid inputs to 0 safely.",
        callout_style
    ))
    story.append(Paragraph(
        "<b>Hurdle D (Model Loading Dependency Bug):</b> Running the web application prior to executing the ML training "
        "pipeline originally caused server crashes due to a missing <i>model.pkl</i> file. We fixed this by placing a "
        "try-except block at server startup that checks for <i>FileNotFoundError</i>, logs a user warning, and disables "
        "inference cleanly rather than hard-crashing.",
        callout_style
    ))
    story.append(Paragraph(
        "<b>Hurdle E (Windows OS File Permission Lockout):</b> During PDF compilation, ReportLab threw a <i>PermissionError "
        "(Errno 13)</i> when the target <i>draft_report.pdf</i> file was actively open in the IDE/viewer. We resolved this by "
        "redirecting the compiler to write to a dedicated file (<i>draft_report_completed.pdf</i>) to prevent write-lock collisions.",
        callout_style
    ))
    
    story.append(Paragraph("<b>3. Project Configuration Settings:</b>", h2_style))
    story.append(Paragraph(
        "• <b>XGBoost Model Tuning:</b> Hyperparameters were locked in <i>config.py</i>: <i>n_estimators=100</i>, "
        "<i>max_depth=6</i>, and <i>eval_metric='logloss'</i>. The explicit evaluation metric suppresses warnings in newer "
        "XGBoost versions and specifies binary cross-entropy loss optimization.<br/>"
        "• <b>Path Portability:</b> The config file dynamically resolves paths using <i>os.path.dirname(os.path.abspath(__file__))</i>, "
        "ensuring the training and serving scripts function seamlessly on any user machine without hardcoding path structures.<br/>"
        "• <b>Dependency Separation:</b> An isolated Python virtual environment (<i>venv/</i>) was established, separating core libraries "
        "(Pandas, Scikit-Learn, XGBoost, and Flask) from global system packages.",
        body_style
    ))
    
    story.append(Paragraph("<b>4. Technical Breakthroughs:</b>", h2_style))
    story.append(Paragraph(
        "• <b>XGBoost Classifier Integration:</b> Achieved a robust <b>90.52% accuracy</b>, significantly outperforming linear models "
        "by capturing non-linear interactions (e.g., follower/following ratios and digit counts).<br/>"
        "• <b>Zero Training-Serving Skew:</b> Implemented a unified feature engineering module (<i>src/feature_engineer.py</i>) "
        "shared between the training script and the prediction engine, guaranteeing identical feature scaling and data columns "
        "in both training and inference contexts.",
        body_style
    ))
    
    story.append(PageBreak())

    # STEP 4
    story.append(Paragraph("Step 4: Testing & Data Collection", h1_style))
    
    story.append(Paragraph("<b>1. Data Collection & Dataset Composition:</b>", h2_style))
    story.append(Paragraph(
        "The dataset used to train and validate Fake Profile Detector consists of a benchmark corpus of <b>576 unique Instagram accounts</b>. "
        "To ensure robust classifier convergence and prevent model bias, the dataset is perfectly balanced: it contains "
        "exactly <b>288 legitimate profiles (Class 0)</b> and <b>288 fake/spam profiles (Class 1)</b>.<br/>"
        "The raw attributes collected cover three key profile dimensions:<br/>"
        "• <i>Binary Indicators:</i> presence of a profile picture, external bio URL, and account privacy setting.<br/>"
        "• <i>Integer Metadata Counts:</i> total postings count, follower count, and follows count.<br/>"
        "• <i>Text-Derived Attributes:</i> bio biography character count, full name word count, and username/fullname digit-to-length ratios.",
        body_style
    ))
    story.append(Paragraph(
        "During ingestion via <i>data_loader.py</i>, raw CSV data tables are parsed into Pandas dataframes. "
        "The data pipeline cleans the records and verifies feature data types. It ensures all input vectors "
        "contain only numerical values (integers or floating-point decimals) prior to training, preventing data formatting exceptions.",
        body_style
    ))
    
    story.append(Paragraph("<b>2. Testing & Validation Methodology:</b>", h2_style))
    story.append(Paragraph(
        "To perform strict validation, the dataset was split using an <b>80/20 partitioning strategy</b>. "
        "A total of <b>80% (460 rows)</b> of the data was allocated to the training partition, allowing the XGBoost "
        "decision trees to learn behavioral feature boundaries. The remaining <b>20% (116 rows)</b> of the records was "
        "withheld as a hidden validation partition, simulating real-world unseen production traffic.<br/>"
        "To guarantee exact reproducibility across runs, the partition split was locked using a random seed value "
        "of <i>random_state = 42</i>. The validation metrics are evaluated by computing:<br/>"
        "• <b>Precision:</b> measures prediction exactness (out of all profiles flagged as fake, what percentage are actually fake). "
        "Formula: <i>TP / (TP + FP)</i>.<br/>"
        "• <b>Recall:</b> measures prediction completeness (out of all actual fake profiles, what percentage did the model catch). "
        "Formula: <i>TP / (TP + FN)</i>.<br/>"
        "• <b>F1-Score:</b> the harmonic mean of precision and recall. Formula: <i>2 * (Precision * Recall) / (Precision + Recall)</i>.<br/>"
        "• <b>Support:</b> the real counts of occurrences in the evaluation split (63 real, 53 fake).",
        body_style
    ))
    
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>3. Quantitative Model Metrics:</b>", h2_style))
    story.append(Paragraph(
        "The model was evaluated on the hidden validation set, obtaining an **overall accuracy of 90.52%** (105 out of 116 "
        "cases classified correctly):",
        body_style
    ))
    
    # Metrics Table
    metrics_data = [
        [
            Paragraph("Metric", table_header_style), 
            Paragraph("Real Profiles (Class 0)", table_header_style), 
            Paragraph("Fake Profiles (Class 1)", table_header_style), 
            Paragraph("Weighted Avg", table_header_style)
        ],
        [Paragraph("Precision", table_cell_bold_style), Paragraph("0.89", table_cell_style), Paragraph("0.92", table_cell_style), Paragraph("0.91", table_cell_style)],
        [Paragraph("Recall", table_cell_bold_style), Paragraph("0.94", table_cell_style), Paragraph("0.87", table_cell_style), Paragraph("0.91", table_cell_style)],
        [Paragraph("F1-Score", table_cell_bold_style), Paragraph("0.91", table_cell_style), Paragraph("0.89", table_cell_style), Paragraph("0.90", table_cell_style)],
        [Paragraph("Support", table_cell_bold_style), Paragraph("63", table_cell_style), Paragraph("53", table_cell_style), Paragraph("116", table_cell_style)]
    ]
    
    t_metrics = Table(metrics_data, colWidths=[120, 130, 130, 120])
    t_metrics.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), primary_color),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('BOTTOMPADDING', (0,0), (-1,0), 3),
        ('TOPPADDING', (0,0), (-1,0), 3),
        ('GRID', (0,0), (-1,-1), 0.5, border_color),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, bg_light]),
        ('TOPPADDING', (0,1), (-1,-1), 3),
        ('BOTTOMPADDING', (0,1), (-1,-1), 3),
    ]))
    story.append(t_metrics)
    story.append(Spacer(1, 4))
    
    story.append(Paragraph("<b>Analysis of Metrics:</b>", h2_style))
    story.append(Paragraph(
        "• <b>High Recall for Real Profiles (0.94):</b> This indicates that only 6% of real users are accidentally flagged as bots (low false positive rate). This is highly desirable in production systems, as blocking legitimate users causes frustration.<br/>"
        "• <b>High Precision for Fake Profiles (0.92):</b> This means that when the model flags a profile as 'Fake', it is correct 92% of the time.",
        body_style
    ))
    
    story.append(PageBreak())  # Put the comprehensive UAT table on its own page (Page 5) to avoid spacing constraints

    # COMPREHENSIVE UAT SECTION
    story.append(Paragraph("User Acceptance Testing (UAT) Verification Cases", h1_style))
    story.append(Paragraph(
        "To verify model robustness and boundary conditions, UAT validation cases were executed. "
        "The table below represents the **complete list of all 11 features** mapped for each scenario to demonstrate "
        "how raw metrics affect the model's ultimate prediction:",
        body_style
    ))
    
    # Transposed Table data to support all 11 features on a portrait page layout
    uat_transposed_data = [
        [
            Paragraph("Parameter / Output", table_header_style), 
            Paragraph("Case 1: Standard User", table_header_style), 
            Paragraph("Case 2: Follow Spammer", table_header_style), 
            Paragraph("Case 3: Empty Bio Bot", table_header_style), 
            Paragraph("Case 4: Balanced Private", table_header_style)
        ],
        [Paragraph("Profile Picture?", table_cell_bold_style), Paragraph("Yes (1)", table_cell_style), Paragraph("No (0)", table_cell_style), Paragraph("No (0)", table_cell_style), Paragraph("Yes (1)", table_cell_style)],
        [Paragraph("Username Digit Ratio", table_cell_bold_style), Paragraph("0.00", table_cell_style), Paragraph("0.35", table_cell_style), Paragraph("0.50", table_cell_style), Paragraph("0.00", table_cell_style)],
        [Paragraph("Full Name Words", table_cell_bold_style), Paragraph("2", table_cell_style), Paragraph("0", table_cell_style), Paragraph("1", table_cell_style), Paragraph("2", table_cell_style)],
        [Paragraph("Full Name Digit Ratio", table_cell_bold_style), Paragraph("0.00", table_cell_style), Paragraph("0.00", table_cell_style), Paragraph("0.00", table_cell_style), Paragraph("0.00", table_cell_style)],
        [Paragraph("Name == Username?", table_cell_bold_style), Paragraph("No (0)", table_cell_style), Paragraph("No (0)", table_cell_style), Paragraph("No (0)", table_cell_style), Paragraph("No (0)", table_cell_style)],
        [Paragraph("Bio Char Length", table_cell_bold_style), Paragraph("45", table_cell_style), Paragraph("0", table_cell_style), Paragraph("0", table_cell_style), Paragraph("60", table_cell_style)],
        [Paragraph("External URL in Bio?", table_cell_bold_style), Paragraph("Yes (1)", table_cell_style), Paragraph("No (0)", table_cell_style), Paragraph("No (0)", table_cell_style), Paragraph("No (0)", table_cell_style)],
        [Paragraph("Is Account Private?", table_cell_bold_style), Paragraph("No (0)", table_cell_style), Paragraph("No (0)", table_cell_style), Paragraph("No (0)", table_cell_style), Paragraph("Yes (1)", table_cell_style)],
        [Paragraph("Number of Posts", table_cell_bold_style), Paragraph("120", table_cell_style), Paragraph("0", table_cell_style), Paragraph("1", table_cell_style), Paragraph("45", table_cell_style)],
        [Paragraph("Number of Followers", table_cell_bold_style), Paragraph("450", table_cell_style), Paragraph("1", table_cell_style), Paragraph("10", table_cell_style), Paragraph("150", table_cell_style)],
        [Paragraph("Number of Follows", table_cell_bold_style), Paragraph("380", table_cell_style), Paragraph("4500", table_cell_style), Paragraph("250", table_cell_style), Paragraph("180", table_cell_style)],
        [Paragraph("<b>Expected Class</b>", table_cell_bold_style), Paragraph("Real", table_cell_style), Paragraph("Fake", table_cell_style), Paragraph("Fake", table_cell_style), Paragraph("Real", table_cell_style)],
        [Paragraph("<b>ML Prediction</b>", table_cell_bold_style), Paragraph("Real (Class 0)", table_cell_style), Paragraph("Fake (Class 1)", table_cell_style), Paragraph("Fake (Class 1)", table_cell_style), Paragraph("Real (Class 0)", table_cell_style)],
        [Paragraph("<b>UAT Verdict Status</b>", table_cell_bold_style), Paragraph("<font color='green'><b>Passed</b></font>", table_cell_style), Paragraph("<font color='green'><b>Passed</b></font>", table_cell_style), Paragraph("<font color='green'><b>Passed</b></font>", table_cell_style), Paragraph("<font color='green'><b>Passed</b></font>", table_cell_style)]
    ]
    
    t_uat = Table(uat_transposed_data, colWidths=[160, 86, 86, 86, 86])
    t_uat.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), primary_color),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('BOTTOMPADDING', (0,0), (-1,0), 3),
        ('TOPPADDING', (0,0), (-1,0), 3),
        ('GRID', (0,0), (-1,-1), 0.5, border_color),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, bg_light]),
        ('TOPPADDING', (0,1), (-1,-1), 3),
        ('BOTTOMPADDING', (0,1), (-1,-1), 3),
    ]))
    story.append(t_uat)
    
    story.append(Spacer(1, 10))
    story.append(Paragraph("<b>Future Recommendations & Extensions:</b>", h2_style))
    story.append(Paragraph(
        "• <b>Natural Language Processing (NLP):</b> Incorporate sentiment and keyword analysis on the biography string to detect spam links or fraudulent offers.<br/>"
        "• <b>Visual CNN Layer:</b> Add a secondary convolutional neural network to evaluate the profile picture for generic stock photos or missing image features.<br/>"
        "• <b>Dynamic API Ingestion:</b> Integrate a background queue to query Instagram's public JSON endpoint to automatically load metrics by username.",
        body_style
    ))
    
    story.append(Spacer(1, 10))
    story.append(Paragraph("<b>Conclusion:</b>", h1_style))
    story.append(Paragraph(
        "Fake Profile Detector successfully demonstrates that machine learning, specifically the <b>XGBoost Classifier</b>, "
        "is an effective tool for identifying automated bot accounts on Instagram using only publicly available metadata. "
        "By engineering features such as the follower/following and posts/following ratios, the model successfully "
        "differentiates complex bot patterns from legitimate user accounts with an out-of-sample accuracy of <b>90.52%</b>. "
        "The serialized model loading architecture allows for rapid, sub-100ms predictions in production, making it a "
        "highly scalable and practical defense mechanism against social media spam and fraud.",
        body_style
    ))
    
    doc.build(story)
    print("Detailed and complete UAT PDF Report generated successfully!")

if __name__ == "__main__":
    generate_report()
