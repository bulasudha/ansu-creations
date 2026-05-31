import os
from pathlib import Path
from zipfile import ZipFile
from textwrap import dedent

# Setup directories
current_dir = Path.cwd()
base = current_dir / "Ansu_Dimension_Premium"
base.mkdir(exist_ok=True)

assets = base / "assets"
assets.mkdir(exist_ok=True)

# 1. Create index.html
(base / "index.html").write_text(dedent("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ansu Dimension | Create. Share. Sell.</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

    <!-- Navigation Bar -->
    <nav class="navbar">
        <div class="logo">Ansu <span>Dimension</span></div>
        <ul class="nav-links">
            <li><a href="#home">Home</a></li>
            <li><a href="#about">About</a></li>
            <li><a href="#services">Services</a></li>
            <li><a href="#shop">Shop</a></li>
            <li><a href="#gallery">Gallery</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
    </nav>

    <!-- Hero Section -->
    <header id="home" class="hero">
        <div class="hero-container">
            <div class="hero-text">
                <span class="badge">The Future of Content</span>
                <h1>Next-Gen AI Video & Digital Creation</h1>
                <p>We craft high-impact AI videos, build viral social media content, and offer premium digital products designed to scale your brand.</p>
                <div class="hero-buttons">
                    <a href="#shop" class="btn btn-primary">Explore Shop</a>
                    <a href="#services" class="btn btn-secondary">Our Services</a>
                </div>
            </div>
            <div class="hero-image">
                <img src="assets/hero-illustration.svg" alt="Ansu Dimension Illustration">
            </div>
        </div>
    </header>

    <!-- About Section -->
    <section id="about" class="about">
        <div class="container">
            <h2>Who We Are</h2>
            <div class="line"></div>
            <p class="section-desc">Ansu Dimension is a creative hub exploring the boundaries of AI-driven media, YouTube growth, and curated digital solutions.</p>
            <div class="about-grid">
                <div class="about-box">
                    <h3>Our Vision</h3>
                    <p>To empower creators worldwide by blending artificial intelligence with beautiful artistic expression.</p>
                </div>
                <div class="about-box">
                    <h3>Our Mission</h3>
                    <p>Delivering premium content automation templates, high-quality digital crafts, and strategic growth assets.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Services Section -->
    <section id="services" class="services">
        <div class="container">
            <h2>Our Specialized Services</h2>
            <div class="line"></div>
            <div class="grid">
                <div class="card service-card">
                    <div class="icon">🤖</div>
                    <h3>AI Video Creation</h3>
                    <p>Cinematic AI generation, workflow optimization, and high-quality rendering for storytelling.</p>
                </div>
                <div class="card service-card">
                    <div class="icon">📺</div>
                    <h3>YouTube & TikTok Growth</h3>
                    <p>Niche research, custom high-CTR thumbnails, and video editing built to capture audience attention.</p>
                </div>
                <div class="card service-card">
                    <div class="icon">🚀</div>
                    <h3>Digital Branding</h3>
                    <p>Social media content design, assets packaging, and automation tool setup for modern online businesses.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Shop Section -->
    <section id="shop" class="shop">
        <div class="container">
            <h2>Featured Digital Products</h2>
            <div class="line"></div>
            <div class="grid">
                <div class="card product-card">
                    <img src="assets/prod-templates.svg" alt="Product 1">
                    <div class="product-info">
                        <span class="prod-tag">Templates</span>
                        <h3>AI Video Prompts Pack</h3>
                        <p>Master text-to-video tools with 500+ ultra-realistic prompts.</p>
                        <div class="price-row">
                            <span class="price">$15.00</span>
                            <button class="btn-buy" onclick="buyItem('AI Video Prompts Pack')">Buy Now</button>
                        </div>
                    </div>
                </div>
                <div class="card product-card">
                    <img src="assets/prod-lut.svg" alt="Product 2">
                    <div class="product-info">
                        <span class="prod-tag">Presets</span>
                        <h3>Cinematic LUTs Pack</h3>
                        <p>Premium color grading configurations for TikTok and Shorts creators.</p>
                        <div class="price-row">
                            <span class="price">$9.00</span>
                            <button class="btn-buy" onclick="buyItem('Cinematic LUTs Pack')">Buy Now</button>
                        </div>
                    </div>
                </div>
                <div class="card product-card">
                    <img src="assets/prod-crafts.svg" alt="Product 3">
                    <div class="product-info">
                        <span class="prod-tag">Art</span>
                        <h3>Digital Crafts & Graphics</h3>
                        <p>Exclusive futuristic element packs and background designs.</p>
                        <div class="price-row">
                            <span class="price">$12.00</span>
                            <button class="btn-buy" onclick="buyItem('Digital Crafts Pack')">Buy Now</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Gallery Section -->
    <section id="gallery" class="gallery">
        <div class="container">
            <h2>Creative Dimensions Gallery</h2>
            <div class="line"></div>
            <div class="gallery-grid">
                <div class="gallery-item"><img src="assets/gal-1.svg" alt="AI Creation 1"></div>
                <div class="gallery-item"><img src="assets/gal-2.svg" alt="AI Creation 2"></div>
                <div class="gallery-item"><img src="assets/gal-3.svg" alt="AI Creation 3"></div>
                <div class="gallery-item"><img src="assets/gal-4.svg" alt="AI Creation 4"></div>
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="contact">
        <div class="container">
            <h2>Let's Connect</h2>
            <div class="line"></div>
            <div class="contact-wrapper">
                <form class="contact-form" onsubmit="handleForm(event)">
                    <input type="text" placeholder="Your Name" required>
                    <input type="email" placeholder="Your Email" required>
                    <textarea placeholder="Tell us about your project or inquiry..." rows="5" required></textarea>
                    <button type="submit" class="btn btn-primary">Send Message</button>
                </form>
                <div class="contact-info">
                    <h3>Get in Touch Directly</h3>
                    <p>Have questions about products, business inquiries, or custom orders?</p>
                    <a href="https://wa.me/#" class="btn-whatsapp" target="_blank">💬 Chat on WhatsApp</a>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <p>&copy; 2026 Ansu Dimension. All Rights Reserved. Designed with modern aesthetics.</p>
    </footer>

    <script src="script.js"></script>
</body>
</html>
"""), encoding="utf-8")

# 2. Create style.css
(base / "style.css").write_text(dedent("""
/* Global Styles & Variables */
:root {
    --bg-main: #0f172a;
    --bg-surface: #1e293b;
    --bg-nav: #0b0f19;
    --primary: #3b82f6;
    --primary-hover: #2563eb;
    --accent: #a855f7;
    --text-light: #f8fafc;
    --text-muted: #94a3b8;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background-color: var(--bg-main);
    color: var(--text-light);
    line-height: 1.6;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 60px 20px;
}

h2 {
    text-align: center;
    font-size: 2.5rem;
    font-weight: 700;
    letter-spacing: 1px;
}

.line {
    width: 60px;
    height: 4px;
    background: linear-gradient(90deg, var(--primary), var(--accent));
    margin: 15px auto 30px auto;
    border-radius: 2px;
}

.section-desc {
    text-align: center;
    color: var(--text-muted);
    max-width: 60px 0;
    margin-bottom: 40px;
}

/* Navbar */
.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 20px 40px;
    background-color: var(--bg-nav);
    position: sticky;
    top: 0;
    z-index: 1000;
    border-bottom: 1px solid #1e293b;
}

.navbar .logo {
    font-size: 1.5rem;
    font-weight: bold;
    letter-spacing: 1px;
}

.navbar .logo span {
    color: var(--primary);
}

.nav-links {
    display: flex;
    list-style: none;
    gap: 25px;
}

.nav-links a {
    color: var(--text-light);
    text-decoration: none;
    font-weight: 500;
    transition: color 0.3s ease;
}

.nav-links a:hover {
    color: var(--primary);
}

/* Hero Section */
.hero {
    background: radial-gradient(circle at top right, #1e1b4b, var(--bg-main));
    padding: 80px 40px;
    min-height: 85vh;
    display: flex;
    align-items: center;
}

.hero-container {
    max-width: 1200px;
    margin: 0 auto;
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 40px;
}

.hero-text {
    flex: 1;
    min-width: 300px;
}

.badge {
    background: rgba(168, 85, 247, 0.2);
    color: var(--accent);
    padding: 6px 12px;
    border-radius: 20px;
    font-size: 0.85rem;
    font-weight: bold;
    display: inline-block;
    margin-bottom: 20px;
}

.hero-text h1 {
    font-size: 3.5rem;
    line-height: 1.2;
    margin-bottom: 20px;
    background: linear-gradient(135deg, #fff, var(--text-muted));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-text p {
    color: var(--text-muted);
    font-size: 1.1rem;
    margin-bottom: 30px;
}

.hero-buttons {
    display: flex;
    gap: 15px;
}

.hero-image {
    flex: 1;
    min-width: 300px;
    display: flex;
    justify-content: center;
}

.hero-image img {
    width: 100%;
    max-width: 450px;
    animation: floating 4s ease-in-out infinite;
}

/* Buttons */
.btn {
    padding: 12px 28px;
    border-radius: 8px;
    font-weight: 600;
    text-decoration: none;
    display: inline-block;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    cursor: pointer;
}

.btn-primary {
    background-color: var(--primary);
    color: white;
    border: none;
}

.btn-primary:hover {
    background-color: var(--primary-hover);
    transform: translateY(-2px);
}

.btn-secondary {
    background-color: transparent;
    color: white;
    border: 2px solid #334155;
}

.btn-secondary:hover {
    background-color: #334155;
    transform: translateY(-2px);
}

/* Cards & Grid Layouts */
.grid {
    display: flex;
    flex-wrap: wrap;
    gap: 30px;
    justify-content: center;
    margin-top: 40px;
}

.card {
    background-color: var(--bg-surface);
    border: 1px solid #334155;
    border-radius: 16px;
    overflow: hidden;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card:hover {
    transform: translateY(-8px);
    box-shadow: 0 10px 25px -5px rgba(59, 130, 246, 0.2);
}

/* About Section */
.about-grid {
    display: flex;
    gap: 20px;
    flex-wrap: wrap;
    margin-top: 30px;
}

.about-box {
    flex: 1;
    min-width: 280px;
    background: linear-gradient(145deg, #1e293b, #0f172a);
    padding: 30px;
    border-radius: 12px;
    border: 1px solid #1e293b;
}

.about-box h3 {
    margin-bottom: 10px;
    color: var(--accent);
}

/* Service Card */
.service-card {
    width: 350px;
    padding: 35px 25px;
    text-align: center;
}

.service-card .icon {
    font-size: 3rem;
    margin-bottom: 15px;
}

.service-card h3 {
    margin-bottom: 12px;
}

.service-card p {
    color: var(--text-muted);
}

/* Product Card */
.product-card {
    width: 350px;
    display: flex;
    flex-direction: column;
}

.product-card img {
    width: 100%;
    height: 200px;
    object-fit: cover;
    background: #111827;
}

.product-info {
    padding: 25px;
}

.prod-tag {
    font-size: 0.75rem;
    background: rgba(59, 130, 246, 0.15);
    color: var(--primary);
    padding: 4px 8px;
    border-radius: 4px;
    font-weight: bold;
}

.product-info h3 {
    margin: 12px 0 8px 0;
}

.product-info p {
    color: var(--text-muted);
    font-size: 0.95rem;
    margin-bottom: 20px;
    height: 50px;
}

.price-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.price {
    font-size: 1.4rem;
    font-weight: bold;
    color: #34d399;
}

.btn-buy {
    background-color: #10b981;
    color: white;
    border: none;
    padding: 8px 16px;
    border-radius: 6px;
    cursor: pointer;
    font-weight: bold;
    transition: background 0.2s;
}

.btn-buy:hover {
    background-color: #059669;
}

/* Gallery Section */
.gallery-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 20px;
    margin-top: 30px;
}

.gallery-item {
    border-radius: 12px;
    overflow: hidden;
    height: 200px;
    border: 2px solid #334155;
    transition: border-color 0.3s;
}

.gallery-item img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.4s ease;
}

.gallery-item:hover img {
    transform: scale(1.08);
}

.gallery-item:hover {
    border-color: var(--accent);
}

/* Contact Section */
.contact-wrapper {
    display: flex;
    flex-wrap: wrap;
    gap: 40px;
    margin-top: 30px;
}

.contact-form {
    flex: 2;
    min-width: 300px;
    display: flex;
    flex-direction: column;
    gap: 15px;
}

.contact-form input, .contact-form textarea {
    background-color: var(--bg-surface);
    border: 1px solid #334155;
    padding: 15px;
    border-radius: 8px;
    color: white;
    font-size: 1rem;
    outline: none;
}

.contact-form input:focus, .contact-form textarea:focus {
    border-color: var(--primary);
}

.contact-info {
    flex: 1;
    min-width: 250px;
    background-color: var(--bg-nav);
    padding: 30px;
    border-radius: 12px;
    border: 1px solid #1e293b;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.contact-info h3 {
    margin-bottom: 15px;
}

.contact-info p {
    color: var(--text-muted);
    margin-bottom: 25px;
}

.btn-whatsapp {
    background-color: #25d366;
    color: white;
    text-decoration: none;
    padding: 12px 20px;
    border-radius: 8px;
    text-align: center;
    font-weight: bold;
    transition: opacity 0.2s;
}

.btn-whatsapp:hover {
    opacity: 0.9;
}

/* Footer */
footer {
    text-align: center;
    padding: 30px;
    background-color: var(--bg-nav);
    border-top: 1px solid #1e293b;
    color: var(--text-muted);
    font-size: 0.9rem;
}

/* Floating Animation */
@keyframes floating {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-15px); }
}

/* Responsive adjustment */
@media (max-width: 768px) {
    .navbar { flex-direction: column; gap: 15px; }
    .hero-text h1 { font-size: 2.5rem; }
}
"""), encoding="utf-8")

# 3. Create script.js
(base / "script.js").write_text(dedent("""
function buyItem(itemName) {
    alert('Thank you for choosing Ansu Dimension! Direct payment setup or redirection path for "' + itemName + '" will trigger here.');
}

function handleForm(event) {
    event.preventDefault();
    alert('Message successfully intercepted! In production, this can automatically pass configurations via formspree or a localized mail engine.');
    event.target.reset();
}
"""), encoding="utf-8")

# 4. Generate custom layout SVG placeholders for items
def make_svg(path, text, bg_color):
    content = dedent(f"""
    <svg xmlns="http://www.w3.org/2000/svg" width="600" height="400">
        <rect width="100%" height="100%" fill="{bg_color}"/>
        <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle"
        font-size="32" fill="white" font-family="'Segoe UI', Arial, sans-serif">{text}</text>
    </svg>
    """).strip()
    path.write_text(content, encoding="utf-8")

make_svg(assets / "hero-illustration.svg", "ANSU DIMENSION AI", "#1e1b4b")
make_svg(assets / "prod-templates.svg", "Prompt Bundle Placeholder", "#2563eb")
make_svg(assets / "prod-lut.svg", "LUT Asset Preview", "#7c3aed")
make_svg(assets / "prod-crafts.svg", "Digital Asset Placeholder", "#db2777")
make_svg(assets / "gal-1.svg", "Dimension Render 01", "#0369a1")
make_svg(assets / "gal-2.svg", "Dimension Render 02", "#0f766e")
make_svg(assets / "gal-3.svg", "Dimension Render 03", "#b45309")
make_svg(assets / "gal-4.svg", "Dimension Render 04", "#4d7c0f")

# Pack inside the final target deployment zip
zip_path = current_dir / "Ansu_Dimension_Premium.zip"
with ZipFile(zip_path, "w") as z:
    for f in base.rglob("*"):
        z.write(f, f.relative_to(base))

print(f"🎉 Success! The ultimate modern layout pack is generated here: {zip_path}")
"""), encoding="utf-8")

# How to use instructions
print("Script successfully formatted.")
