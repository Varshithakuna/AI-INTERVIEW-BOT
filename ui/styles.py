def load_css():

    return """
    <style>

    /* -----------------------------
       Google Font
    ----------------------------- */

    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    html, body, [class*="css"]{
        font-family:'Inter',sans-serif;
    }

    /* -----------------------------
       Background
    ----------------------------- */

    .stApp{
        background:#0B1120;
    }

    .main{
        background:#0B1120;
    }

    .block-container{
        max-width:1250px;
        padding-top:2rem;
        padding-bottom:2rem;
    }

    /* -----------------------------
       Header
    ----------------------------- */

    .title{

        font-size:48px;

        font-weight:700;

        color:white;

        text-align:center;

        margin-bottom:8px;
    }

    .subtitle{

        text-align:center;

        color:#94A3B8;

        font-size:18px;

        margin-bottom:40px;
    }

    /* -----------------------------
       Cards
    ----------------------------- */

    .card{

        background:#111827;

        border:1px solid #1F2937;

        border-radius:20px;

        padding:28px;

        margin-bottom:25px;

        transition:0.3s;

        box-shadow:
        0px 8px 30px rgba(0,0,0,.45);

    }

    .card:hover{

        transform:translateY(-3px);

        border:1px solid #4F46E5;

        box-shadow:
        0px 15px 35px rgba(79,70,229,.25);

    }

    /* -----------------------------
       Card Heading
    ----------------------------- */

    .card h2{

        color:white;

        font-size:24px;

        margin-bottom:20px;
    }

    /* -----------------------------
       Labels
    ----------------------------- */

    label{

        color:#E5E7EB !important;

        font-weight:600 !important;

    }

    /* -----------------------------
       Inputs
    ----------------------------- */

    .stTextInput input{

        background:#1F2937 !important;

        color:white !important;

        border-radius:12px;

        border:1px solid #374151;

        height:48px;
    }

    .stTextArea textarea{

        background:#1F2937 !important;

        color:white !important;

        border-radius:12px;

        border:1px solid #374151;
    }

    .stSelectbox div[data-baseweb="select"]{

        background:#1F2937;

        border-radius:12px;

    }

    /* -----------------------------
       Buttons
    ----------------------------- */

    .stButton>button{

        width:100%;

        height:54px;

        border:none;

        border-radius:14px;

        background:linear-gradient(90deg,#6366F1,#8B5CF6);

        color:white;

        font-size:17px;

        font-weight:600;

        transition:.3s;

    }

    .stButton>button:hover{

        transform:translateY(-2px);

        box-shadow:0px 12px 30px rgba(99,102,241,.35);

    }

    /* -----------------------------
       AI Chat
    ----------------------------- */

    .chat-ai{

        background:#111827;

        border-left:5px solid #6366F1;

        color:white;

        padding:22px;

        border-radius:18px;

        margin-bottom:18px;

        line-height:1.8;

        font-size:16px;

    }

    /* -----------------------------
       User Chat
    ----------------------------- */

    .chat-user{

        background:#1D4ED8;

        color:white;

        padding:20px;

        border-radius:18px;

        margin-bottom:18px;

    }

    /* -----------------------------
       Progress
    ----------------------------- */

    .stProgress > div > div > div{

        background:#6366F1;

    }

    /* -----------------------------
       Metrics
    ----------------------------- */

    div[data-testid="metric-container"]{

        background:#111827;

        border:1px solid #1F2937;

        border-radius:16px;

        padding:18px;

    }

    /* -----------------------------
       Divider
    ----------------------------- */

    hr{

        border:1px solid #1F2937;

    }

    </style>
    """