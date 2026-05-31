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
