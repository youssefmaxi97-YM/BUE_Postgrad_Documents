import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Inject the Logo HTML at the top of the container
logo_html = """        <div class="logo-container">
            <img src="./BUE.png" alt="British University in Egypt Logo" class="bue-logo">
        </div>
        """
content = content.replace('<h1 id="main-heading">', logo_html + '<h1 id="main-heading">')

# 2. Add Logo CSS
logo_css = """
        .logo-container {
            display: flex;
            justify-content: center;
            margin-bottom: 1.5rem;
        }
        .bue-logo {
            max-width: 180px;
            height: auto;
            object-fit: contain;
        }
"""
content = content.replace("/* Typography */", logo_css + "\n        /* Typography */")

# 3. Modify Tabs Structure -> Vertical List
# Remove old tab header gradients
content = re.sub(r"/\* Gradient fades.*?\*/.*?\.tabs-header-wrapper::after.*?\}", "", content, flags=re.DOTALL)

# Refactor CSS for Vertical Tabs Menu
vertical_tabs_css = """
        .layout-grid {
            display: grid;
            grid-template-columns: 200px 1fr;
            gap: 1.5rem;
            align-items: start;
        }

        .tabs-header-wrapper {
            position: relative;
        }

        .tabs-header {
            display: flex;
            flex-direction: column;
            gap: 0.5rem;
            max-height: 450px;
            overflow-y: auto;
            padding-right: 0.5rem;
            scrollbar-width: thin;
            scrollbar-color: rgba(0, 51, 102, 0.2) transparent;
        }

        .tabs-header::-webkit-scrollbar {
            width: 6px;
        }
        .tabs-header::-webkit-scrollbar-thumb {
            background-color: rgba(0, 51, 102, 0.2);
            border-radius: 10px;
        }

        .tab-btn {
            background: rgba(0, 0, 0, 0.02);
            border: 1px solid rgba(0, 0, 0, 0.05);
            color: var(--text-muted);
            padding: 0.8rem 1rem;
            border-radius: 12px;
            font-size: 0.85rem;
            font-weight: 500;
            text-align: left;
            white-space: normal;
            line-height: 1.3;
            cursor: pointer;
            transition: all 0.3s ease;
            font-family: 'Inter', sans-serif;
            width: 100%;
        }

        .tab-btn:hover {
            background: rgba(0, 0, 0, 0.05);
            color: var(--text-main);
            transform: translateX(2px);
        }

        .tab-btn.active {
            background: var(--bue-blue);
            color: #fff;
            border-color: var(--bue-blue);
            box-shadow: 0 4px 12px rgba(0, 51, 102, 0.15);
            transform: translateX(4px);
        }

        @media (max-width: 768px) {
            .layout-grid {
                grid-template-columns: 1fr;
            }
            .tabs-header {
                max-height: 250px;
            }
            .tab-btn.active {
                transform: translateX(0);
            }
            .tab-btn:hover {
                transform: translateX(0);
            }
            .container {
                padding: 2rem 1.25rem;
            }
        }
"""
content = re.sub(r"\.tabs-header-wrapper \{.*?(?=\.tab-content \{)", vertical_tabs_css, content, flags=re.DOTALL)

# Also widen the container slightly for the new 2-column layout
content = content.replace("max-width: 650px;", "max-width: 850px;")

# 4. Update the Javascript rendering to include the new layout-grid wrapper
js_refactor = """
        const tabsContainer = document.getElementById('tabs-container');
        
        // Wrap everything in a CSS Grid (.layout-grid)
        let htmlStr = `<div class="layout-grid">`;

        // Left Sidebar (Vertical Menu)
        htmlStr += `<div class="tabs-header-wrapper"><div class="tabs-header" id="tabs-header">`;
        files.forEach((fileObj, index) => {
            htmlStr += `<button class="tab-btn ${index === 0 ? 'active' : ''}" onclick="switchTab(${index})" id="btn-${index}">${generateShortName(fileObj.name)}</button>`;
        });
        htmlStr += `</div></div>`;

        // Right Content Area
        htmlStr += `<div class="tabs-contents-wrapper">`;
        files.forEach((fileObj, index) => {
            htmlStr += `
                <div class="tab-content ${index === 0 ? 'active' : ''}" id="tab-content-${index}">
                    <div class="file-icon">${getIconForFile(fileObj.name)}</div>
                    <h3 class="file-name">${fileObj.name}</h3>
                    <p class="file-note">This file will open directly in Google Drive</p>
                    <div class="btn-container">
                        <a href="${fileObj.link}" target="_blank" rel="noopener noreferrer" class="btn" title="Open File">
                            <span>Open File to View</span>
                            <svg fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path>
                            </svg>
                        </a>
                    </div>
                </div>
            `;
        });
        htmlStr += `</div></div>`;

        tabsContainer.innerHTML = htmlStr;

        window.switchTab = (index) => {
            document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
            document.querySelectorAll('.tab-content').forEach(content => content.classList.remove('active'));
            
            const btn = document.getElementById(`btn-${index}`);
            const content = document.getElementById(`tab-content-${index}`);
            
            btn.classList.add('active');
            content.classList.add('active');

            // Scroll active tab into view in the sidebar
            btn.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        };
"""
content = re.sub(r"const tabsContainer = document.getElementById\('tabs-container'\);.*?<\/script>", js_refactor + "\n    </script>", content, flags=re.DOTALL)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Applied Vertical Grid Layout and Logo.")
