COCOON_LOGO_DATA_URL = (
    "data:image/jpeg;base64,"
    "/9j/4AAQSkZJRgABAQACWAJYAAD/4QAC/9sAhAAIBgYHBgUIBwcHCQkICgwUDQwLCwwZEhMPFB0aHx4d"
    "GhwcICQuJyAiLCMcHCg3KSwwMTQ0NB8nOT04Mjwu/9sAhAAJCQkMCwwYDQ0YOCgfKDgoODg4ODg4ODg4"
    "ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4/8AAEQgBSAEsAwEiAAIRAQMRAf/EAB8A"
    "AAIDAAMBAQEBAAAAAAAAAAUGBwgBAwQICf/EAMMQAAIBAwMCBAQEBQMDAwQDAAECAwAEEQUSIRMxBkFR"
    "YXGBIjKRoQdCwfAVI1Ki0VKS4fAzgpKi8UNTc7L/xAAZAQADAQEBAAAAAAAAAAAAAAAAAQIDBAX/xAAk"
    "EQEBAAICAgIDAQEBAAAAAAAAAQIRAyExEkFRIlFxYf/aAAwDAQACEQMRAD8A9xREQBERAEREAREQBERA"
    "EREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQH//Z"
)

PANEL_HTML = f"""<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8"/>
<title>Cocoon • Secure Encryption</title>
<meta name="viewport" content="width=device-width,initial-scale=1,user-scalable=no"/>
<script src="https://telegram.org/js/telegram-web-app.js"></script>
<script src="https://unpkg.com/@tonconnect/sdk@latest/dist/tonconnect-sdk.min.js"></script>
<style>

:root{{
--bg-main:#0a0a0a;
--bg-secondary:#0f0f0f;
--bg-card:#1a1a1a;
--bg-card-hover:#1f1f1f;
--bg-elevated:#242424;
--accent:#0088cc;
--accent-hover:#0099e6;
--accent-light:rgba(0,136,204,0.15);
--accent-glow:rgba(0,136,204,0.4);
--success:#10b981;
--success-light:rgba(16,185,129,0.15);
--warning:#f59e0b;
--error:#ef4444;
--text-primary:#ffffff;
--text-secondary:#a0a0a0;
--text-tertiary:#707070;
--text-muted:#505050;
--border:rgba(255,255,255,0.08);
--border-strong:rgba(255,255,255,0.12);
--shadow-sm:0 1px 3px rgba(0,0,0,0.3);
--shadow-md:0 4px 16px rgba(0,0,0,0.4);
--shadow-lg:0 8px 32px rgba(0,0,0,0.5);
--shadow-xl:0 12px 48px rgba(0,0,0,0.6);
--shadow-glow:0 0 24px var(--accent-glow);
--radius-sm:12px;
--radius-md:16px;
--radius-lg:20px;
--radius-xl:24px;
--radius-full:9999px;
--transition-fast:0.15s cubic-bezier(0.4,0,0.2,1);
--transition-base:0.25s cubic-bezier(0.4,0,0.2,1);
--transition-slow:0.35s cubic-bezier(0.4,0,0.2,1);
}}

[data-theme="light"]{{
--bg-main:#f8f9fa;
--bg-secondary:#f5f5f5;
--bg-card:#ffffff;
--bg-card-hover:#fafafa;
--bg-elevated:#ffffff;
--accent:#0088cc;
--accent-hover:#0099e6;
--accent-light:rgba(0,136,204,0.1);
--accent-glow:rgba(0,136,204,0.3);
--success:#10b981;
--success-light:rgba(16,185,129,0.1);
--warning:#f59e0b;
--error:#ef4444;
--text-primary:#0a0a0a;
--text-secondary:#666666;
--text-tertiary:#999999;
--text-muted:#b0b0b0;
--border:rgba(0,0,0,0.08);
--border-strong:rgba(0,0,0,0.12);
--shadow-sm:0 1px 2px rgba(0,0,0,0.05);
--shadow-md:0 4px 12px rgba(0,0,0,0.08);
--shadow-lg:0 8px 24px rgba(0,0,0,0.1);
--shadow-xl:0 12px 40px rgba(0,0,0,0.12);
--shadow-glow:0 0 20px var(--accent-glow);
}}

*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}

html{{
font-size:16px;
-webkit-font-smoothing:antialiased;
-moz-osx-font-smoothing:grayscale;
text-rendering:optimizeLegibility;
}}

body{{
font-family:-apple-system,BlinkMacSystemFont,"SF Pro Display","Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;
background:var(--bg-main);
color:var(--text-primary);
line-height:1.6;
overflow-x:hidden;
transition:background var(--transition-base),color var(--transition-base);
}}

.app-container{{
min-height:100vh;
display:flex;
flex-direction:column;
max-width:720px;
margin:0 auto;
padding:env(safe-area-inset-top) env(safe-area-inset-right) env(safe-area-inset-bottom) env(safe-area-inset-left);
}}

/* ============ HEADER ============ */
.header{{
position:sticky;
top:0;
z-index:100;
background:var(--bg-secondary);
backdrop-filter:blur(20px) saturate(180%);
border-bottom:1px solid var(--border);
padding:16px 20px;
display:flex;
align-items:center;
justify-content:space-between;
gap:16px;
box-shadow:var(--shadow-sm);
}}

.header-left{{
display:flex;
align-items:center;
gap:12px;
}}

.avatar{{
width:44px;
height:44px;
border-radius:var(--radius-full);
background:url('{COCOON_LOGO_DATA_URL}') center/cover no-repeat;
box-shadow:0 0 0 2px var(--bg-secondary),0 0 0 4px var(--accent-light),var(--shadow-glow);
transition:transform var(--transition-fast);
flex-shrink:0;
}}

.avatar:hover{{
transform:scale(1.05);
}}

.header-title{{
display:flex;
flex-direction:column;
gap:2px;
}}

.app-name{{
font-size:20px;
font-weight:700;
letter-spacing:-0.03em;
color:var(--text-primary);
}}

.app-subtitle{{
font-size:11px;
font-weight:500;
letter-spacing:0.05em;
text-transform:uppercase;
color:var(--text-tertiary);
}}

.header-right{{
display:flex;
align-items:center;
gap:8px;
}}

.user-badge{{
  display:none;
}}
.wallet-btn{{
  padding:6px 14px;
  border-radius:var(--radius-full);
  background:transparent;
  border:1px solid var(--border);
  font-size:13px;
  font-weight:600;
  color:var(--text-secondary);
  display:flex;
  align-items:center;
  gap:6px;
  cursor:pointer;
  transition:all var(--transition-fast);
}}

.wallet-btn.connected{{
  background:var(--accent-light);
  color:var(--accent);
  border-color:rgba(0,136,204,0.5);
}}

.wallet-btn:hover{{
  background:var(--bg-card-hover);
  border-color:var(--accent);
  color:var(--accent);
  transform:translateY(-1px);
  box-shadow:var(--shadow-sm);
}}

.wallet-btn:active{{
  transform:scale(0.96);
}}


.user-badge:hover{{
background:var(--accent);
color:#ffffff;
border-color:var(--accent);
transform:translateY(-1px);
box-shadow:var(--shadow-glow);
}}

.theme-toggle{{
.lang-toggle{{
  min-width:48px;
  height:32px;
  padding:0 10px;
  border-radius:var(--radius-full);
  background:var(--bg-card);
  border:1px solid var(--border);
  display:flex;
  align-items:center;
  justify-content:center;
  cursor:pointer;
  font-size:13px;
  font-weight:600;
  color:var(--text-secondary);
  transition:all var(--transition-fast);
}}

.lang-toggle:hover{{
  background:var(--bg-card-hover);
  border-color:var(--accent);
  color:var(--accent);
  box-shadow:var(--shadow-sm);
}}

.lang-toggle:active{{
  transform:scale(0.96);
}}

width:40px;
height:40px;
border-radius:var(--radius-full);
background:var(--bg-card);
border:1px solid var(--border);
display:flex;
align-items:center;
justify-content:center;
cursor:pointer;
font-size:18px;
transition:all var(--transition-fast);
}}

.theme-toggle:hover{{
background:var(--bg-card-hover);
border-color:var(--accent);
transform:scale(1.1);
box-shadow:var(--shadow-md);
}}

.theme-toggle:active{{
transform:scale(0.95);
}}

/* ============ TABS ============ */
.tabs-container{{
padding:16px 20px 0;
}}

.tabs{{
  position:relative;
  display:grid;
  grid-template-columns:repeat(3,1fr);
  gap:6px;
  padding:4px;
  background:var(--bg-card);
  border-radius:var(--radius-lg);
  border:1px solid var(--border);
  box-shadow:var(--shadow-md);
  overflow:hidden;
}}

/* индикатор активной вкладки */
.tab-indicator{{
  position:absolute;
  top:4px;
  left:4px;
  height:calc(100% - 8px);
  border-radius:calc(var(--radius-lg) - 4px);
  background:linear-gradient(135deg,var(--accent) 0%,var(--accent-hover) 100%);
  box-shadow:var(--shadow-glow),inset 0 1px 0 rgba(255,255,255,0.1);
  z-index:0;
  pointer-events:none;
  transition:all var(--transition-base);
}}

/* вкладки поверх индикатора */
.tab{{
  text-align:center;
  padding:12px 8px;
  font-size:14px;
  font-weight:600;
  letter-spacing:-0.01em;
  border-radius:calc(var(--radius-lg) - 4px);
  color:var(--text-secondary);
  cursor:pointer;
  user-select:none;
  transition:color var(--transition-fast);
  position:relative;
  z-index:1;
  display:flex;
  align-items:center;
  justify-content:center;
  gap:6px;
  white-space:nowrap;
}}

.tab.active{{
  color:#ffffff;
  text-shadow:0 1px 2px rgba(0,0,0,0.2);
}}

.tab:not(.active):hover{{
  color:var(--text-primary);
}}




.tab{{
text-align:center;
padding:12px 8px;
font-size:14px;
font-weight:600;
letter-spacing:-0.01em;
border-radius:calc(var(--radius-lg) - 4px);
color:var(--text-secondary);
cursor:pointer;
user-select:none;
transition:color var(--transition-fast);
position:relative;
z-index:1;
display:flex;
align-items:center;
justify-content:center;
gap:6px;
white-space:nowrap;
}}

.tab.active{{
color:#ffffff;
text-shadow:0 1px 2px rgba(0,0,0,0.2);
}}

.tab:not(.active):hover{{
color:var(--text-primary);
}}

/* ============ CONTENT ============ */
.content{{
flex:1;
padding:20px;
}}

.tab-body{{
display:none;
flex-direction:column;
gap:20px;
opacity:0;
transform:translateY(10px);
transition:opacity var(--transition-base),transform var(--transition-base);
}}

.tab-body.active{{
display:flex;
opacity:1;
transform:translateY(0);
}}

/* ============ CARDS ============ */
.card{{
background:var(--bg-card);
border-radius:var(--radius-xl);
border:1px solid var(--border);
padding:24px;
box-shadow:var(--shadow-md);
transition:all var(--transition-base);
position:relative;
overflow:hidden;
}}

.card::before{{
content:"";
position:absolute;
top:0;
left:0;
right:0;
height:1px;
background:linear-gradient(90deg,transparent 0%,var(--border-strong) 50%,transparent 100%);
opacity:0.5;
}}

.card:hover{{
border-color:var(--border-strong);
box-shadow:var(--shadow-lg);
}}

.card-header{{
display:flex;
justify-content:space-between;
align-items:flex-start;
margin-bottom:20px;
gap:16px;
}}

.card-title-group{{
flex:1;
}}

.card-title{{
font-size:20px;
font-weight:700;
letter-spacing:-0.02em;
color:var(--text-primary);
margin-bottom:6px;
}}

.card-subtitle{{
font-size:13px;
color:var(--text-secondary);
line-height:1.5;
}}

.status-badge{{
padding:8px 14px;
border-radius:var(--radius-full);
font-size:12px;
font-weight:600;
white-space:nowrap;
display:flex;
align-items:center;
gap:6px;
transition:all var(--transition-fast);
}}

.status-badge.success{{
background:var(--success-light);
border:1px solid rgba(16,185,129,0.3);
color:var(--success);
}}

.status-badge.inactive{{
background:var(--accent-light);
border:1px solid rgba(0,136,204,0.2);
color:var(--text-tertiary);
}}

.status-badge:hover{{
transform:scale(1.05);
}}

/* ============ INPUTS ============ */
.input-group{{
margin-top:4px;
}}

.textarea{{
width:100%;
min-height:180px;
padding:16px;
resize:vertical;
border:1px solid var(--border);
border-radius:var(--radius-md);
background:var(--bg-elevated);
color:var(--text-primary);
font-size:15px;
font-family:inherit;
line-height:1.6;
outline:none;
transition:all var(--transition-fast);
box-shadow:inset 0 1px 3px rgba(0,0,0,0.2);
}}

.textarea:hover{{
border-color:var(--border-strong);
background:var(--bg-card-hover);
}}

.textarea:focus{{
border-color:var(--accent);
background:var(--bg-card);
box-shadow:0 0 0 4px var(--accent-light),inset 0 1px 3px rgba(0,0,0,0.1);
}}

.textarea::placeholder{{
color:var(--text-muted);
}}

.input{{
width:100%;
padding:12px 16px;
border:1px solid var(--border);
border-radius:var(--radius-md);
background:var(--bg-elevated);
color:var(--text-primary);
font-size:15px;
font-family:inherit;
outline:none;
transition:all var(--transition-fast);
box-shadow:inset 0 1px 2px rgba(0,0,0,0.15);
}}

.input:hover{{
border-color:var(--border-strong);
background:var(--bg-card-hover);
}}

.input:focus{{
border-color:var(--accent);
background:var(--bg-card);
box-shadow:0 0 0 4px var(--accent-light),inset 0 1px 2px rgba(0,0,0,0.1);
}}

.input::placeholder{{
color:var(--text-muted);
}}

/* ============ BUTTONS ============ */
.button-group{{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(140px,1fr));
gap:12px;
margin-top:16px;
}}

.btn{{
position:relative;
display:flex;
align-items:center;
justify-content:center;
gap:8px;
padding:14px 20px;
border:none;
border-radius:var(--radius-md);
font-size:15px;
font-weight:600;
font-family:inherit;
cursor:pointer;
user-select:none;
overflow:hidden;
transition:all var(--transition-fast);
}}

.btn::before{{
content:"";
position:absolute;
inset:0;
background:radial-gradient(circle at center,rgba(255,255,255,0.25) 0%,transparent 70%);
opacity:0;
transition:opacity var(--transition-fast);
}}

.btn:active::before{{
opacity:1;
}}

.btn-primary{{
background:linear-gradient(135deg,var(--accent) 0%,var(--accent-hover) 100%);
color:#ffffff;
box-shadow:var(--shadow-glow),inset 0 1px 0 rgba(255,255,255,0.1);
}}

.btn-primary:hover{{
transform:translateY(-2px);
box-shadow:0 0 32px var(--accent-glow),var(--shadow-lg),inset 0 1px 0 rgba(255,255,255,0.2);
}}

.btn-primary:active{{
transform:translateY(0);
}}

.btn-secondary{{
background:var(--bg-elevated);
color:var(--text-primary);
border:1px solid var(--border);
box-shadow:var(--shadow-sm);
}}

.btn-secondary:hover{{
background:var(--bg-card-hover);
border-color:var(--accent);
color:var(--accent);
transform:translateY(-1px);
box-shadow:var(--shadow-md);
}}

.btn-secondary:active{{
transform:scale(0.98);
}}

.btn:disabled,.btn.disabled{{
opacity:0.4;
cursor:not-allowed;
transform:none!important;
}}

.btn-icon{{
width:40px;
height:40px;
padding:0;
border-radius:var(--radius-full);
}}

/* ============ PROGRESS ============ */
.progress-bar{{
height:4px;
background:var(--accent-light);
border-radius:var(--radius-full);
overflow:hidden;
margin-top:16px;
display:none;
}}

.progress-bar.active{{
display:block;
}}

.progress-fill{{
height:100%;
background:linear-gradient(90deg,var(--accent) 0%,var(--accent-hover) 100%);
border-radius:var(--radius-full);
width:0%;
animation:progress 1.5s ease-in-out;
box-shadow:0 0 12px var(--accent-glow);
}}

@keyframes progress{{
0%{{width:0%}}
50%{{width:70%}}
100%{{width:100%}}
}}

/* ============ OUTPUT ============ */
.output-block{{
margin-top:20px;
padding:20px;
border-radius:var(--radius-md);
background:var(--bg-elevated);
border:1px solid var(--border);
box-shadow:inset 0 1px 3px rgba(0,0,0,0.2);
position:relative;
overflow:hidden;
}}

.output-block::before{{
content:"";
position:absolute;
top:0;
left:0;
right:0;
height:1px;
background:linear-gradient(90deg,transparent 0%,var(--accent-light) 50%,transparent 100%);
}}

.output-label{{
font-size:12px;
font-weight:600;
letter-spacing:0.05em;
text-transform:uppercase;
color:var(--text-tertiary);
margin-bottom:12px;
display:flex;
align-items:center;
gap:8px;
}}

.output-value{{
font-family:"SF Mono",ui-monospace,Menlo,Monaco,Consolas,monospace;
font-size:13px;
color:var(--text-primary);
word-break:break-all;
line-height:1.7;
}}

/* ============ HINTS ============ */
.hint{{
font-size:13px;
color:var(--text-secondary);
margin-top:12px;
padding:12px 16px;
border-radius:var(--radius-sm);
background:var(--accent-light);
border:1px solid rgba(0,136,204,0.2);
display:flex;
align-items:center;
gap:10px;
animation:slideIn 0.3s ease;
}}

.hint.success{{
background:var(--success-light);
border-color:rgba(16,185,129,0.3);
color:var(--success);
}}

.hint.error{{
background:rgba(239,68,68,0.15);
border-color:rgba(239,68,68,0.3);
color:var(--error);
}}

@keyframes slideIn{{
from{{opacity:0;transform:translateY(-10px)}}
to{{opacity:1;transform:translateY(0)}}
}}

/* ============ CHAT ============ */
.chat-header{{
display:flex;
justify-content:space-between;
align-items:center;
gap:12px;
margin-bottom:16px;
}}

.chat-room-info{{
font-size:13px;
font-weight:600;
color:var(--text-secondary);
padding:8px 14px;
border-radius:var(--radius-full);
background:var(--accent-light);
border:1px solid rgba(0,136,204,0.2);
}}

.chat-share{{
font-size:12px;
color:var(--text-tertiary);
margin-top:12px;
padding:12px;
border-radius:var(--radius-sm);
background:rgba(255,255,255,0.02);
border:1px solid var(--border);
word-break:break-all;
line-height:1.6;
}}

.chat-box{{
margin-top:16px;
padding:20px;
border-radius:var(--radius-md);
background:var(--bg-elevated);
border:1px solid var(--border);
max-height:400px;
min-height:200px;
overflow-y:auto;
display:flex;
flex-direction:column;
gap:16px;
box-shadow:inset 0 2px 4px rgba(0,0,0,0.2);
}}

.chat-message{{
display:flex;
width:100%;
animation:messageSlide 0.3s ease;
}}

@keyframes messageSlide{{
from{{opacity:0;transform:translateY(10px)}}
to{{opacity:1;transform:translateY(0)}}
}}

.chat-message.me{{
justify-content:flex-end;
}}

.chat-message.other{{
justify-content:flex-start;
}}

.message-bubble{{
max-width:75%;
padding:12px 16px;
border-radius:18px;
font-size:15px;
line-height:1.5;
word-wrap:break-word;
white-space:pre-wrap;
}}

.chat-message.other .message-bubble{{
background:var(--bg-elevated);
border:1px solid var(--border);
color:var(--text-primary);
border-bottom-left-radius:4px;
}}

.chat-message.me .message-bubble{{
background:linear-gradient(135deg,var(--accent) 0%,var(--accent-hover) 100%);
color:#ffffff;
border-bottom-right-radius:4px;
box-shadow:var(--shadow-glow);
}}

.message-meta{{
font-size:11px;
font-weight:600;
margin-bottom:4px;
opacity:0.7;
}}

.chat-input-row{{
display:flex;
gap:12px;
margin-top:16px;
}}

.chat-input-row .input{{
flex:1;
}}

/* ============ FOOTER ============ */
.footer{{
margin-top:auto;
padding:24px 20px;
text-align:center;
font-size:13px;
color:var(--text-tertiary);
line-height:1.7;
border-top:1px solid var(--border);
}}

/* ============ SPLASH ============ */
.splash{{
position:fixed;
inset:0;
z-index:9999;
display:flex;
flex-direction:column;
align-items:center;
justify-content:center;
background:linear-gradient(180deg,var(--bg-secondary) 0%,var(--bg-main) 100%);
animation:splashFade 2.5s ease forwards;
}}

.splash-logo{{
max-width:min(300px,70vw);
height:auto;
margin-bottom:32px;
filter:drop-shadow(var(--shadow-glow));
animation:logoFloat 3s ease-in-out infinite;
}}

@keyframes logoFloat{{
0%,100%{{transform:translateY(0)}}
50%{{transform:translateY(-10px)}}
}}

.splash-title{{
font-size:36px;
font-weight:700;
letter-spacing:-0.03em;
background:linear-gradient(135deg,var(--accent) 0%,var(--accent-hover) 100%);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
background-clip:text;
}}

@keyframes splashFade{{
0%{{opacity:0}}
20%{{opacity:1}}
80%{{opacity:1}}
100%{{opacity:0;visibility:hidden}}
}}

/* ============ SCROLLBAR ============ */
::-webkit-scrollbar{{
width:10px;
height:10px;
}}

::-webkit-scrollbar-track{{
background:transparent;
}}

::-webkit-scrollbar-thumb{{
background:rgba(255,255,255,0.1);
border-radius:var(--radius-full);
border:2px solid transparent;
background-clip:padding-box;
}}

::-webkit-scrollbar-thumb:hover{{
background:rgba(255,255,255,0.2);
background-clip:padding-box;
}}

/* ============ MOBILE ============ */
@media(max-width:640px){{
.header{{
padding:12px 16px;
}}

.avatar{{
width:40px;
height:40px;
}}

.app-name{{
font-size:18px;
}}

.content{{
padding:16px;
}}

.card{{
padding:20px;
border-radius:var(--radius-lg);
}}

.tab{{
font-size:13px;
padding:10px 6px;
}}

.button-group{{
grid-template-columns:1fr;
}}

.textarea{{
min-height:140px;
font-size:14px;
}}

.input{{
font-size:14px;
}}

.output-block{{
padding:16px;
}}

.chat-box{{
max-height:300px;
min-height:160px;
padding:16px;
}}

.message-bubble{{
font-size:14px;
padding:10px 14px;
}}
}}

/* ============ UTILITIES ============ */
.hidden{{
display:none!important;
}}

.fade-in{{
animation:fadeIn 0.3s ease;
}}

@keyframes fadeIn{{
from{{opacity:0}}
to{{opacity:1}}
}}
</style>
</head>
<body>

<!-- Splash Screen -->
<div id="splash" class="splash">
<img class="splash-logo" src="https://raw.githubusercontent.com/gradolz95-png/cocoon-assets/main/000025_1764570763_751668_big-no-bg-preview%20(carve.photos)%20(2).png" alt="Cocoon"/>
<div class="splash-title">Cocoon</div>
</div>

<!-- Main App -->
<div class="app-container hidden" id="app">

<!-- Header -->
<header class="header">
<div class="header-left">
<div class="avatar" id="avatar"></div>
<div class="header-title">
<div class="app-name">Cocoon</div>
<div class="app-subtitle">End-to-End Encryption</div>
</div>
</div>
<div class="header-right">
  <div class="user-badge" id="user-badge">
    <span>👤</span>
    <span id="user-name">гость</span>
  </div>
  <button class="wallet-btn" id="wallet-connect">
    <span>💎</span>
    <span id="wallet-label">TON</span>
  </button>
  <div class="theme-toggle" id="theme-toggle">🌙</div>
</div>


</header>

<!-- Tabs -->
<div class="tabs-container">
  <div class="tabs" id="tabs">
    <div class="tab-indicator" id="tab-indicator"></div>
    <div class="tab active" id="tab-encrypt">🔒 Шифрование</div>
    <div class="tab" id="tab-decrypt">🔓 Расшифровка</div>
    <div class="tab" id="tab-chat">💬 Чат</div>
  </div>
</div>


<!-- Content -->
<main class="content">

<!-- Encrypt Tab -->
<section class="tab-body active" id="body-encrypt">
<div class="card">
<div class="card-header">
<div class="card-title-group">
<div class="card-title" id="encrypt-title">Создать шифр</div>
<div class="card-subtitle" id="encrypt-subtitle">Текст шифруется локально, ключ хранится только в сессии</div>
</div>
<div class="status-badge inactive" id="key-status">
<span>🔑</span>
<span id="key-status-text">не инициализирован</span>
</div>
</div>

<div class="input-group">
<textarea class="textarea" id="plain-input" placeholder="Введи текст, который хочешь зашифровать..."></textarea>
</div>

<div class="progress-bar" id="progress-encrypt">
<div class="progress-fill"></div>
</div>

<div class="button-group">
<button class="btn btn-primary" id="btn-encrypt">
<span>🔒</span>
<span id="btn-encrypt-text">Зашифровать</span>
</button>
<button class="btn btn-secondary disabled" id="btn-share" disabled>
<span>✉️</span>
<span id="btn-share-text">Отправить</span>
</button>
</div>

<div class="button-group">
<button class="btn btn-secondary disabled" id="btn-copy" disabled>
<span>📋</span>
<span id="btn-copy-text">Скопировать</span>
</button>
<button class="btn btn-secondary" id="btn-reset">
<span>♻️</span>
<span id="btn-reset-text">Сбросить ключ</span>
</button>
</div>

<div class="output-block">
<div class="output-label">
<span>📦</span>
<span id="encrypt-output-label">Зашифрованный текст</span>
</div>
<div class="output-value" id="cipher-output">Пока ничего не зашифровано.</div>
</div>

<div id="copy-hint-container"></div>
</div>
</section>


<!-- Decrypt Tab -->
<section class="tab-body" id="body-decrypt">
<div class="card">
<div class="card-header">
<div class="card-title-group">
<div class="card-title" id="decrypt-title">Расшифровать шифр</div>
<div class="card-subtitle" id="decrypt-subtitle">Вставь строку формата cocoon:v1:...</div>
</div>
</div>

<div class="input-group">
<textarea class="textarea" id="cipher-input" placeholder="Вставь шифр, который хочешь расшифровать..."></textarea>
</div>

<div class="progress-bar" id="progress-decrypt">
<div class="progress-fill"></div>
</div>

<div class="button-group">
<button class="btn btn-primary" id="btn-decrypt">
<span>🔓</span>
<span id="btn-decrypt-text">Расшифровать</span>
</button>
<button class="btn btn-secondary" id="btn-clear-dec">
<span>🧹</span>
<span id="btn-clear-dec-text">Очистить</span>
</button>
</div>

<div class="button-group">
<button class="btn btn-secondary" id="btn-paste">
<span>📥</span>
<span id="btn-paste-text">Вставить из буфера</span>
</button>
</div>

<div class="output-block">
<div class="output-label">
<span>📄</span>
<span id="decrypt-output-label">Исходный текст</span>
</div>
<div class="output-value" id="plain-output">Пока ничего не расшифровано.</div>
</div>
</div>
</section>



<!-- Chat Tab -->
<section class="tab-body" id="body-chat">
<div class="card">
<div class="card-header">
<div class="card-title-group">
<div class="card-title" id="chat-title">Секретная комната</div>
<div class="card-subtitle" id="chat-subtitle">Ссылка содержит ключ, сервер видит только шифр</div>
</div>
</div>

<div class="chat-header">
<button class="btn btn-primary" id="btn-create-room">
<span>🔑</span>
<span id="btn-create-room-text">Создать комнату</span>
</button>
<div class="chat-room-info" id="chat-room-label">Комната не выбрана</div>
</div>

<div class="chat-share" id="chat-share-link"></div>

<div class="progress-bar" id="progress-chat">
<div class="progress-fill"></div>
</div>

<div class="chat-box" id="chat-box">
<div id="chat-empty-text" style="font-size:13px;color:var(--text-tertiary);text-align:center">
Чтобы начать, создай комнату или открой ссылку от друга.<br/>
Текст в комнате шифруется на твоей стороне.
</div>
</div>

<div class="chat-input-row">
<input class="input" id="chat-input" placeholder="Сообщение..."/>
<button class="btn btn-primary" id="btn-send-chat">
<span>📤</span>
<span id="btn-send-chat-text">Отправить</span>
</button>
</div>
</div>
</section>


</main>

<!-- Footer -->
<footer class="footer" id="footer-text">
🔐 Cocoon не хранит твои ключи в базе.<br/>
Панель шифрует текст в браузере, чат-комнаты — в e2e-режиме отправляют только шифр.
</footer>


</div>

<script>
// ============ INITIALIZATION ============
const tg = window.Telegram?.WebApp;
let cocoonUser = {{ name: "гость", id: null }};

// ============ CHAT PAYWALL / TON ============
const CHAT_PAYWALL_ENABLED = true; // сделай false, если чат должен быть бесплатным
const CHAT_PRICE_NANOTON = "100000000"; // 0.1 TON в нанотонах
const CHAT_RECEIVER_ADDRESS = "EQ____________________________"; // сюда подставь свой TON-адрес

let tonConnector = null;
let tonWallet = null;


// ============ HAPTIC FEEDBACK ============
function haptic(type) {{
  if (!tg?.HapticFeedback) return;

  const types = {{
    light: () => tg.HapticFeedback.impactOccurred("light"),
    medium: () => tg.HapticFeedback.impactOccurred("medium"),
    heavy: () => tg.HapticFeedback.impactOccurred("heavy"),
    success: () => tg.HapticFeedback.notificationOccurred("success"),
    error: () => tg.HapticFeedback.notificationOccurred("error"),
  }};

  types[type]?.();
}}

// ============ PROGRESS BAR ============
function showProgress(id) {{
  const el = document.getElementById(id);
  if (!el) return;

  el.classList.add("active");
  setTimeout(() => el.classList.remove("active"), 1500);
}}

// ============ SPLASH SCREEN ============
window.addEventListener("load", () => {{
  const splash = document.getElementById("splash");
  const app = document.getElementById("app");

  setTimeout(() => {{
    splash?.remove();
    app?.classList.remove("hidden");
  }}, 2500);
}});

// ============ USER INITIALIZATION ============
function setDefaultAvatar() {{
  const avatar = document.getElementById("avatar");
  if (avatar) {{
    avatar.style.backgroundImage = "url('{COCOON_LOGO_DATA_URL}')";
  }}
}}

if (tg) {{
  tg.ready();
  tg.expand();

  const user = tg.initDataUnsafe?.user;
  if (user) {{
    const name = [user.first_name, user.last_name].filter(Boolean).join(" ");
    cocoonUser.name = name || "Без имени";
    cocoonUser.id = user.id;

    document.getElementById("user-name").textContent = cocoonUser.name;

    const avatar = document.getElementById("avatar");
    if (avatar && user.photo_url) {{
      avatar.style.backgroundImage = `url('${{user.photo_url}}')`;
    }} else {{
      setDefaultAvatar();
    }}
  }} else {{
    setDefaultAvatar();
  }}
}} else {{
  setDefaultAvatar();
}}

// ============ TON CONNECT ============
const walletBtn = document.getElementById("wallet-connect");
const walletLabel = document.getElementById("wallet-label");

function shortTonAddress(addr) {{
  if (!addr) return "TON";
  return addr.slice(0, 4) + "…" + addr.slice(-4);
}}

async function initTonConnect() {{
  if (!window.TonConnectSDK || !walletBtn) return;

  tonConnector = new TonConnectSDK.TonConnect({{
    // положи tonconnect-manifest.json в корень домена или поменяй путь
    manifestUrl: window.location.origin + "/tonconnect-manifest.json",
  }});

  await tonConnector.restoreConnection();

  const updateUi = (wallet) => {{
    tonWallet = wallet || null;

    if (!wallet) {{
      walletBtn.classList.remove("connected");
      walletLabel.textContent = "TON";
      return;
    }}

    walletBtn.classList.add("connected");
    const addr = wallet.account?.address;
    walletLabel.textContent = shortTonAddress(addr);
  }};

  updateUi(tonWallet);

  tonConnector.onStatusChange((wallet) => {{
    updateUi(wallet);
  }});
}}

if (walletBtn) {{
  walletBtn.addEventListener("click", async () => {{
    if (!tonConnector) return;

    // если уже подключен — отключаем
    if (tonWallet) {{
      await tonConnector.disconnect();
      tonWallet = null;
      walletBtn.classList.remove("connected");
      walletLabel.textContent = "TON";
      haptic("light");
      return;
    }}

    try {{
      const wallets = await tonConnector.getWallets();
      const tonkeeper =
        wallets.find((w) => w.name.toLowerCase().includes("tonkeeper")) ||
        wallets[0];

      const link = tonConnector.connect({{
        universalLink: tonkeeper.universalLink,
        bridgeUrl: tonkeeper.bridgeUrl,
      }});

      if (tg?.openTelegramLink) {{
        tg.openTelegramLink(link);
      }} else {{
        window.open(link, "_blank");
      }}
    }} catch (e) {{
      console.error("TonConnect error", e);
      haptic("error");
    }}
  }});
}}

initTonConnect();


// ============ THEME TOGGLE ============
const themeToggle = document.getElementById("theme-toggle");
let currentTheme = localStorage.getItem("cocoon-theme") || "dark";

document.body.setAttribute("data-theme", currentTheme);
themeToggle.textContent = currentTheme === "dark" ? "🌙" : "☀️";

themeToggle.addEventListener("click", () => {{

// ============ I18N ============

const I18N = {{
  ru: {{
    "tab-encrypt": "🔒 Шифрование",
    "tab-decrypt": "🔓 Расшифровка",
    "tab-chat": "💬 Чат",

    "encrypt-title": "Создать шифр",
    "encrypt-subtitle": "Текст шифруется локально, ключ хранится только в сессии",
    "encrypt-placeholder": "Введи текст, который хочешь зашифровать...",
    "btn-encrypt-text": "Зашифровать",
    "btn-share-text": "Отправить",
    "btn-copy-text": "Скопировать",
    "btn-reset-text": "Сбросить ключ",
    "encrypt-output-label": "Зашифрованный текст",
    "cipher-output-empty": "Пока ничего не зашифровано.",

    "decrypt-title": "Расшифровать шифр",
    "decrypt-subtitle": "Вставь строку формата cocoon:v1:...",
    "decrypt-placeholder": "Вставь шифр, который хочешь расшифровать...",
    "btn-decrypt-text": "Расшифровать",
    "btn-clear-dec-text": "Очистить",
    "btn-paste-text": "Вставить из буфера",
    "decrypt-output-label": "Исходный текст",
    "plain-output-empty": "Пока ничего не расшифровано.",

    "chat-title": "Секретная комната",
    "chat-subtitle": "Ссылка содержит ключ, сервер видит только шифр",
    "btn-create-room-text": "Создать комнату",
    "chat-room-label-empty": "Комната не выбрана",
    "chat-empty-text": "Чтобы начать, создай комнату или открой ссылку от друга.<br/>Текст в комнате шифруется на твоей стороне.",
    "chat-input-placeholder": "Сообщение...",
    "btn-send-chat-text": "Отправить",

    "footer-text": "🔐 Cocoon не хранит твои ключи в базе.<br/>Панель шифрует текст в браузере, чат-комнаты — в e2e-режиме отправляют только шифр."
  }},
  en: {{
    "tab-encrypt": "🔒 Encrypt",
    "tab-decrypt": "🔓 Decrypt",
    "tab-chat": "💬 Chat",

    "encrypt-title": "Create cipher",
    "encrypt-subtitle": "Text is encrypted locally, the key lives only in this session",
    "encrypt-placeholder": "Enter the text you want to encrypt...",
    "btn-encrypt-text": "Encrypt",
    "btn-share-text": "Send",
    "btn-copy-text": "Copy",
    "btn-reset-text": "Reset key",
    "encrypt-output-label": "Encrypted text",
    "cipher-output-empty": "Nothing encrypted yet.",

    "decrypt-title": "Decrypt cipher",
    "decrypt-subtitle": "Paste a string in the cocoon:v1:... format",
    "decrypt-placeholder": "Paste the cipher you want to decrypt...",
    "btn-decrypt-text": "Decrypt",
    "btn-clear-dec-text": "Clear",
    "btn-paste-text": "Paste from clipboard",
    "decrypt-output-label": "Original text",
    "plain-output-empty": "Nothing decrypted yet.",

    "chat-title": "Secret room",
    "chat-subtitle": "The link contains the key, the server sees only ciphertext",
    "btn-create-room-text": "Create room",
    "chat-room-label-empty": "No room selected",
    "chat-empty-text": "To start, create a room or open a link from a friend.<br/>Text in the room is encrypted on your side.",
    "chat-input-placeholder": "Message...",
    "btn-send-chat-text": "Send",

    "footer-text": "🔐 Cocoon never stores your keys in a database.<br/>The panel encrypts text in the browser, chat rooms send only ciphertext in end-to-end mode."
  }}
}};

const langToggle = document.getElementById("lang-toggle");
let currentLang = "ru";

function applyLang(lang) {{
  const dict = I18N[lang] || I18N.en;
  currentLang = lang;

  if (langToggle) {{
    langToggle.textContent = lang === "ru" ? "RU" : "EN";
  }}

  const setText = (id, key) => {{
    const el = document.getElementById(id);
    if (el && dict[key]) el.textContent = dict[key];
  }};

  const setHTML = (id, key) => {{
    const el = document.getElementById(id);
    if (el && dict[key]) el.innerHTML = dict[key];
  }};

  const setPlaceholder = (id, key) => {{
    const el = document.getElementById(id);
    if (el && dict[key]) el.setAttribute("placeholder", dict[key]);
  }};

  // tabs
  setText("tab-encrypt", "tab-encrypt");
  setText("tab-decrypt", "tab-decrypt");
  setText("tab-chat", "tab-chat");

  // encrypt
  setText("encrypt-title", "encrypt-title");
  setText("encrypt-subtitle", "encrypt-subtitle");
  setPlaceholder("plain-input", "encrypt-placeholder");
  setText("btn-encrypt-text", "btn-encrypt-text");
  setText("btn-share-text", "btn-share-text");
  setText("btn-copy-text", "btn-copy-text");
  setText("btn-reset-text", "btn-reset-text");
  setText("encrypt-output-label", "encrypt-output-label");
  const cipherOut = document.getElementById("cipher-output");
  if (cipherOut && (cipherOut.textContent === I18N.ru["cipher-output-empty"] || cipherOut.textContent === I18N.en["cipher-output-empty"])) {{
    cipherOut.textContent = dict["cipher-output-empty"];
  }}

  // decrypt
  setText("decrypt-title", "decrypt-title");
  setText("decrypt-subtitle", "decrypt-subtitle");
  setPlaceholder("cipher-input", "decrypt-placeholder");
  setText("btn-decrypt-text", "btn-decrypt-text");
  setText("btn-clear-dec-text", "btn-clear-dec-text");
  setText("btn-paste-text", "btn-paste-text");
  setText("decrypt-output-label", "decrypt-output-label");
  const plainOut = document.getElementById("plain-output");
  if (plainOut && (plainOut.textContent === I18N.ru["plain-output-empty"] || plainOut.textContent === I18N.en["plain-output-empty"])) {{
    plainOut.textContent = dict["plain-output-empty"];
  }}

  // chat
  setText("chat-title", "chat-title");
  setText("chat-subtitle", "chat-subtitle");
  setText("btn-create-room-text", "btn-create-room-text");
  const roomLabel = document.getElementById("chat-room-label");
  if (roomLabel && (roomLabel.textContent === I18N.ru["chat-room-label-empty"] || roomLabel.textContent === I18N.en["chat-room-label-empty"])) {{
    roomLabel.textContent = dict["chat-room-label-empty"];
  }}
  setHTML("chat-empty-text", "chat-empty-text");
  setPlaceholder("chat-input", "chat-input-placeholder");
  setText("btn-send-chat-text", "btn-send-chat-text");

  // footer
  setHTML("footer-text", "footer-text");
}}

function detectLang() {{
  const stored = localStorage.getItem("cocoon-lang");
  if (stored === "ru" || stored === "en") return stored;

  const tgLang = tg?.initDataUnsafe?.user?.language_code;
  const navLang = (navigator.language || navigator.userLanguage || "en").toLowerCase();
  const raw = (tgLang || navLang || "en").toLowerCase();

  if (raw.startsWith("ru")) return "ru";
  return "en";
}}

currentLang = detectLang();
applyLang(currentLang);

if (langToggle) {{
  langToggle.addEventListener("click", () => {{
    haptic("light");
    const next = currentLang === "ru" ? "en" : "ru";
    localStorage.setItem("cocoon-lang", next);
    applyLang(next);
  }});
}}

  haptic("light");
  currentTheme = currentTheme === "dark" ? "light" : "dark";
  document.body.setAttribute("data-theme", currentTheme);
  themeToggle.textContent = currentTheme === "dark" ? "🌙" : "☀️";
  localStorage.setItem("cocoon-theme", currentTheme);
}});

// ============ CLIPBOARD ============
async function copyToClipboard(text) {{
  try {{
    if (navigator.clipboard?.writeText) {{
      await navigator.clipboard.writeText(text);
      return true;
    }}
  }} catch (e) {{}}

  try {{
    const tmp = document.createElement("textarea");
    tmp.value = text;
    tmp.style.position = "fixed";
    tmp.style.left = "-9999px";
    document.body.appendChild(tmp);
    tmp.focus();
    tmp.select();
    tmp.setSelectionRange(0, 99999);
    const success = document.execCommand("copy");
    document.body.removeChild(tmp);
    return success;
  }} catch (e) {{
    return false;
  }}
}}

// ============ ENCRYPTION ============
let sessionKey = null;
let sessionKeyId = null;

async function ensureKey() {{
  if (!sessionKey) {{
    sessionKey = await window.crypto.subtle.generateKey(
      {{ name: "AES-GCM", length: 256 }},
      true,
      ["encrypt", "decrypt"]
    );

    const raw = await window.crypto.subtle.exportKey("raw", sessionKey);
    sessionKeyId = btoa(String.fromCharCode(...new Uint8Array(raw))).replace(/=+$/g, "");

    const statusBadge = document.getElementById("key-status");
    statusBadge.innerHTML = '<span>🔑</span><span>активен</span>';
    statusBadge.classList.remove("inactive");
    statusBadge.classList.add("success");
  }}
}}

function bufToBase64(buf) {{
  return btoa(String.fromCharCode(...new Uint8Array(buf)));
}}

function base64ToBuf(b64) {{
  const bin = atob(b64);
  const arr = new Uint8Array(bin.length);
  for (let i = 0; i < bin.length; i++) arr[i] = bin.charCodeAt(i);
  return arr.buffer;
}}

async function encryptText(plain) {{
  await ensureKey();
  const enc = new TextEncoder().encode(plain);
  const iv = window.crypto.getRandomValues(new Uint8Array(12));
  const ctBuf = await window.crypto.subtle.encrypt(
    {{ name: "AES-GCM", iv }},
    sessionKey,
    enc
  );
  const ivB64 = bufToBase64(iv.buffer);
  const ctB64 = bufToBase64(ctBuf);
  return `cocoon:v1:${{sessionKeyId}}:${{ivB64}}:${{ctB64}}`;
}}

async function decryptText(cipherStr) {{
  try {{
    if (!cipherStr.startsWith("cocoon:v1:")) throw new Error("bad format");

    const parts = cipherStr.split(":");
    if (parts.length !== 5) throw new Error("bad parts");

    const [, , keyId, ivB64, ctB64] = parts;
    const ivBuf = base64ToBuf(ivB64);
    const ctBuf = base64ToBuf(ctB64);

    if (!sessionKey || sessionKeyId !== keyId) {{
      const bin = atob(keyId);
      const raw = new Uint8Array(bin.length);
      for (let i = 0; i < bin.length; i++) raw[i] = bin.charCodeAt(i);

      sessionKey = await window.crypto.subtle.importKey(
        "raw",
        raw.buffer,
        {{ name: "AES-GCM" }},
        true,
        ["encrypt", "decrypt"]
      );
      sessionKeyId = keyId;

      const statusBadge = document.getElementById("key-status");
      statusBadge.innerHTML = '<span>🔑</span><span>импортирован</span>';
      statusBadge.classList.remove("inactive");
      statusBadge.classList.add("success");
    }}

    const ptBuf = await window.crypto.subtle.decrypt(
      {{ name: "AES-GCM", iv: new Uint8Array(ivBuf) }},
      sessionKey,
      ctBuf
    );

    return new TextDecoder().decode(ptBuf);
  }} catch (e) {{
    return null;
  }}
}}

// ============ HINTS ============
function showHint(message, type = "success") {{
  const container = document.getElementById("copy-hint-container");
  if (!container) return;

  const hint = document.createElement("div");
  hint.className = `hint ${{type}}`;

  const icon = type === "success" ? "✅" : type === "error" ? "❌" : "ℹ️";
  hint.innerHTML = `<span>${{icon}}</span><span>${{message}}</span>`;

  container.innerHTML = "";
  container.appendChild(hint);

  setTimeout(() => hint.remove(), 5000);
}}

// ============ TABS ============
const tabs = {{
  encrypt: document.getElementById("tab-encrypt"),
  decrypt: document.getElementById("tab-decrypt"),
  chat: document.getElementById("tab-chat"),
}};

const bodies = {{
  encrypt: document.getElementById("body-encrypt"),
  decrypt: document.getElementById("body-decrypt"),
  chat: document.getElementById("body-chat"),
}};

const tabsEl = document.getElementById("tabs");
const tabIndicator = document.getElementById("tab-indicator");
let currentTabIndex = 0;

function moveIndicator(target) {{
  if (!tabIndicator || !target || !tabsEl) return;
  const tabsRect = tabsEl.getBoundingClientRect();
  const rect = target.getBoundingClientRect();
  const left = rect.left - tabsRect.left;
  const width = rect.width;
  tabIndicator.style.left = `${{left}}px`;
  tabIndicator.style.width = `${{width}}px`;
}}

function activateTab(which) {{
  haptic("light");

  Object.values(tabs).forEach(t => t.classList.remove("active"));
  Object.values(bodies).forEach(b => b.classList.remove("active"));

  const tabMap = {{ encrypt: 0, decrypt: 1, chat: 2 }};
  currentTabIndex = tabMap[which];

  const activeTab = tabs[which];
  activeTab.classList.add("active");
  bodies[which].classList.add("active");

  moveIndicator(activeTab);
}}

tabs.encrypt.addEventListener("click", () => activateTab("encrypt"));
tabs.decrypt.addEventListener("click", () => activateTab("decrypt"));
tabs.chat.addEventListener("click", () => activateTab("chat"));

// Touch swipe
let touchStartX = 0;
let touchEndX = 0;

document.querySelector(".content").addEventListener("touchstart", (e) => {{
  touchStartX = e.changedTouches[0].screenX;
}}, {{ passive: true }});

document.querySelector(".content").addEventListener("touchend", (e) => {{
  touchEndX = e.changedTouches[0].screenX;
  handleSwipe();
}}, {{ passive: true }});

function handleSwipe() {{
  const diff = touchStartX - touchEndX;
  if (Math.abs(diff) < 50) return;

  const order = ["encrypt", "decrypt", "chat"];
  if (diff > 0 && currentTabIndex < 2) {{
    activateTab(order[currentTabIndex + 1]);
  }} else if (diff < 0 && currentTabIndex > 0) {{
    activateTab(order[currentTabIndex - 1]);
  }}
}}

// начальное позиционирование индикатора
moveIndicator(tabs.encrypt);

// ============ ENCRYPT TAB ============
const plainInput = document.getElementById("plain-input");
const cipherOutput = document.getElementById("cipher-output");
const btnEncrypt = document.getElementById("btn-encrypt");
const btnCopy = document.getElementById("btn-copy");
const btnShare = document.getElementById("btn-share");
const btnReset = document.getElementById("btn-reset");

btnEncrypt.addEventListener("click", async () => {{
  const text = plainInput.value.trim();
  if (!text) return;

  haptic("medium");
  btnEncrypt.classList.add("disabled");
  showProgress("progress-encrypt");

  try {{
    const cipher = await encryptText(text);
    cipherOutput.textContent = cipher;

    btnCopy.disabled = false;
    btnCopy.classList.remove("disabled");
    btnShare.disabled = false;
    btnShare.classList.remove("disabled");

    const ok = await copyToClipboard(cipher);
    if (ok) {{
      haptic("success");
      showHint("Шифр автоматически скопирован в буфер обмена!", "success");
    }} else {{
      showHint("Не удалось автоматически скопировать. Используй кнопку 'Скопировать'.", "error");
    }}
  }} finally {{
    btnEncrypt.classList.remove("disabled");
  }}
}});

btnCopy.addEventListener("click", async () => {{
  const cipher = cipherOutput.textContent || "";
  if (!cipher || cipher === "Пока ничего не зашифровано.") return;

  haptic("light");
  const ok = await copyToClipboard(cipher);

  if (ok) {{
    haptic("success");
    showHint("Шифр скопирован в буфер обмена!", "success");
  }} else {{
    haptic("error");
    showHint("Не удалось скопировать. Попробуй выделить текст вручную.", "error");
  }}
}});

btnShare.addEventListener("click", () => {{
  haptic("medium");
  const cipher = cipherOutput.textContent || "";
  if (!cipher || cipher === "Пока ничего не зашифровано.") return;

  const url = "https://t.me/share/url?url=" + encodeURIComponent(cipher);

  if (tg?.openTelegramLink) {{
    tg.openTelegramLink(url);
  }} else {{
    window.open(url, "_blank");
  }}
}});

btnReset.addEventListener("click", () => {{
  haptic("medium");
  sessionKey = null;
  sessionKeyId = null;

  const statusBadge = document.getElementById("key-status");
  statusBadge.innerHTML = '<span>🔑</span><span>не инициализирован</span>';
  statusBadge.classList.remove("success");
  statusBadge.classList.add("inactive");

  showHint("Ключ сброшен. Новый будет создан при следующем шифровании.");
}});

// ============ DECRYPT TAB ============
const cipherInput = document.getElementById("cipher-input");
const plainOutput = document.getElementById("plain-output");
const btnDecrypt = document.getElementById("btn-decrypt");
const btnClearDec = document.getElementById("btn-clear-dec");
const btnPaste = document.getElementById("btn-paste");

btnDecrypt.addEventListener("click", async () => {{
  const c = cipherInput.value.trim();
  if (!c) return;

  haptic("medium");
  btnDecrypt.classList.add("disabled");
  showProgress("progress-decrypt");
  plainOutput.textContent = "Пробую расшифровать...";

  const res = await decryptText(c);

  if (res === null) {{
    haptic("error");
    plainOutput.textContent = "Не получилось расшифровать. Проверь формат шифра.";
  }} else {{
    haptic("success");
    plainOutput.textContent = res;
  }}

  btnDecrypt.classList.remove("disabled");
}});

btnClearDec.addEventListener("click", () => {{
  haptic("light");
  cipherInput.value = "";
  plainOutput.textContent = "Пока ничего не расшифровано.";
}});

btnPaste.addEventListener("click", async () => {{
  haptic("light");

  try {{
    let text = "";

    // Try Telegram WebApp Clipboard
    if (tg?.readTextFromClipboard) {{
      try {{
        text = await new Promise((resolve, reject) => {{
          tg.readTextFromClipboard((clipboardText) => {{
            if (clipboardText) resolve(clipboardText);
            else reject();
          }});
          setTimeout(() => reject(), 2000);
        }});
      }} catch (err) {{
        console.log("Telegram clipboard failed");
      }}
    }}

    // Try Clipboard API
    if (!text && navigator.clipboard?.readText) {{
      try {{
        text = await navigator.clipboard.readText();
      }} catch (err) {{
        console.log("Clipboard API failed");
      }}
    }}

    // Fallback to manual input
    if (!text) {{
      const overlay = document.createElement("div");
      overlay.style.cssText = "position:fixed;inset:0;background:rgba(0,0,0,0.8);backdrop-filter:blur(8px);z-index:9999;display:flex;align-items:center;justify-content:center;padding:20px";

      const modal = document.createElement("div");
      modal.style.cssText = "background:var(--bg-card);border-radius:var(--radius-xl);padding:24px;max-width:500px;width:100%;border:1px solid var(--border);box-shadow:var(--shadow-xl)";

      const title = document.createElement("div");
      title.style.cssText = "font-size:18px;font-weight:700;margin-bottom:16px;color:var(--text-primary)";
      title.textContent = "📥 Вставь шифр";

      const tmp = document.createElement("textarea");
      tmp.className = "textarea";
      tmp.placeholder = "Вставь шифр сюда (долгое нажатие → Вставить)";
      tmp.style.minHeight = "120px";

      const btnRow = document.createElement("div");
      btnRow.style.cssText = "display:flex;gap:12px;margin-top:16px";

      const okBtn = document.createElement("button");
      okBtn.className = "btn btn-primary";
      okBtn.innerHTML = "<span>✓</span><span>Вставить</span>";
      okBtn.style.flex = "1";

      const cancelBtn = document.createElement("button");
      cancelBtn.className = "btn btn-secondary";
      cancelBtn.innerHTML = "<span>✕</span><span>Отмена</span>";
      cancelBtn.style.flex = "1";

      btnRow.appendChild(okBtn);
      btnRow.appendChild(cancelBtn);

      modal.appendChild(title);
      modal.appendChild(tmp);
      modal.appendChild(btnRow);
      overlay.appendChild(modal);
      document.body.appendChild(overlay);

      tmp.focus();

      text = await new Promise((resolve) => {{
        okBtn.onclick = () => {{
          resolve(tmp.value);
          overlay.remove();
        }};
        cancelBtn.onclick = () => {{
          resolve("");
          overlay.remove();
        }};
        overlay.onclick = (e) => {{
          if (e.target === overlay) {{
            resolve("");
            overlay.remove();
          }}
        }};
      }});
    }}

    if (text?.trim()) {{
      cipherInput.value = text.trim();
      haptic("success");

      if (text.trim().startsWith("cocoon:v1:")) {{
        setTimeout(() => btnDecrypt.click(), 300);
      }}
    }} else {{
      haptic("error");
    }}
  }} catch (e) {{
    console.error("Paste error:", e);
    haptic("error");
  }}
}});

// ============ CHAT TAB ============
async function ensureChatPayment() {{
  if (!CHAT_PAYWALL_ENABLED) return true;

  if (!tonConnector || !tonWallet) {{
    showHint("Подключи TON-кошелёк, чтобы создать комнату.", "error");
    haptic("error");
    return false;
  }}

  try {{
    await tonConnector.sendTransaction({{
      validUntil: Math.floor(Date.now() / 1000) + 300,
      messages: [
        {{
          address: CHAT_RECEIVER_ADDRESS,
          amount: CHAT_PRICE_NANOTON,
        }},
      ],
    }});

    haptic("success");
    showHint("Оплата успешно отправлена, чат разблокирован.", "success");
    return true;
  }} catch (e) {{
    console.error("TON payment error", e);
    haptic("error");
    showHint("Транзакция отменена или не прошла.", "error");
    return false;
  }}
}}

const chatBox = document.getElementById("chat-box");
const chatRoomLabel = document.getElementById("chat-room-label");
const chatShareLink = document.getElementById("chat-share-link");
const chatInput = document.getElementById("chat-input");
const btnCreateRoom = document.getElementById("btn-create-room");
const btnSendChat = document.getElementById("btn-send-chat");
let currentRoomId = null;

function renderChatMessage(msg, isMe) {{
  const row = document.createElement("div");
  row.className = `chat-message ${{isMe ? "me" : "other"}}`;

  const bubble = document.createElement("div");
  bubble.className = "message-bubble";

  const meta = document.createElement("div");
  meta.className = "message-meta";
  meta.textContent = (msg.author_name || "Гость") + (msg.time ? " • " + msg.time : "");

  const text = document.createElement("div");
  text.textContent = msg.text;

  bubble.appendChild(meta);
  bubble.appendChild(text);
  row.appendChild(bubble);
  chatBox.appendChild(row);
}}

function clearChatBox() {{
  chatBox.innerHTML = "";
}}

async function loadHistory() {{
  if (!currentRoomId) return;

  try {{
    showProgress("progress-chat");
    const res = await fetch(`/api/room/${{encodeURIComponent(currentRoomId)}}/history`);
    if (!res.ok) return;

    const data = await res.json();
    clearChatBox();

    if (!data.messages?.length) {{
      chatBox.innerHTML = '<div style="font-size:13px;color:var(--text-tertiary);text-align:center">Пока сообщений нет. Напиши что-нибудь первым.</div>';
      return;
    }}

    data.messages.forEach(m => {{
      const isMe = cocoonUser.id && String(m.author_id) === String(cocoonUser.id);
      renderChatMessage(m, isMe);
    }});

    chatBox.scrollTop = chatBox.scrollHeight;
  }} catch (e) {{}}
}}

async function sendChat() {{
  if (!currentRoomId) return;

  const text = chatInput.value.trim();
  if (!text) return;

  haptic("medium");
  chatInput.value = "";

  const payload = {{
    text,
    author_name: cocoonUser.name,
    author_id: cocoonUser.id,
  }};

  try {{
    await fetch(`/api/room/${{encodeURIComponent(currentRoomId)}}/send`, {{
      method: "POST",
      headers: {{ "Content-Type": "application/json" }},
      body: JSON.stringify(payload),
    }});

    renderChatMessage({{
      text,
      author_name: cocoonUser.name,
      author_id: cocoonUser.id,
      time: "",
    }}, true);

    chatBox.scrollTop = chatBox.scrollHeight;
    haptic("success");
  }} catch (e) {{
    haptic("error");
  }}
}}

btnSendChat.addEventListener("click", sendChat);

chatInput.addEventListener("keydown", (e) => {{
  if (e.key === "Enter" && !e.shiftKey) {{
    e.preventDefault();
    sendChat();
  }}
}});

function shortRoom(id) {{
  return id ? id.slice(0, 8) + "…" : "";
}}

async function setupRoomFromParam() {{
  const params = new URLSearchParams(window.location.search);
  const room = params.get("room");

  if (room) {{
    currentRoomId = room;
    chatRoomLabel.textContent = shortRoom(room);
    chatShareLink.textContent = "Поделись этой ссылкой, чтобы подключить других.";
    await loadHistory();
  }}
}}

btnCreateRoom.addEventListener("click", async () => {{
  haptic("heavy");

  const ok = await ensureChatPayment();
  if (!ok) return;

  const rand = crypto.getRandomValues(new Uint8Array(8));
  const hex = Array.from(rand).map(b => b.toString(16).padStart(2, "0")).join("");
  currentRoomId = "room_" + hex;

  const url = window.location.origin + window.location.pathname + "?room=" + encodeURIComponent(currentRoomId);

  chatRoomLabel.textContent = shortRoom(currentRoomId);
  chatShareLink.textContent = url;

  await copyToClipboard(url);

  if (tg?.openTelegramLink) {{
    const shareUrl = "https://t.me/share/url?url=" + encodeURIComponent(url) + "&text=" + encodeURIComponent("Подключайся в секретную комнату Cocoon");
    tg.openTelegramLink(shareUrl);
  }}

  clearChatBox();
  chatBox.innerHTML = '<div style="font-size:13px;color:var(--text-tertiary);text-align:center">Комната создана. Ссылка скопирована, отправь другу.</div>';

  haptic("success");
}});

setupRoomFromParam();
setInterval(loadHistory, 5000);
</script>

</body>
</html>
"""