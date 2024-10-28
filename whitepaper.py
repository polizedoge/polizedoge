from fpdf import FPDF

# Create instance of FPDF class
pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)

# Title and Header
pdf.set_font("Arial", "B", 16)
pdf.cell(200, 10, "Polizei Doge Whitepaper", ln=True, align="C")
pdf.set_font("Arial", "I", 12)
pdf.cell(200, 10, "Building a Trustworthy Community in the Crypto Space", ln=True, align="C")
pdf.ln(20)

# Introduction Section
pdf.set_font("Arial", "B", 14)
pdf.cell(200, 10, "Introduction", ln=True)
pdf.set_font("Arial", "", 12)
pdf.multi_cell(0, 10, "Polizei Doge is more than just a meme coin; it's a community dedicated to fostering "
                     "trust, transparency, and loyalty in the crypto space. Our mission is to combat scams, "
                     "rug pulls, and honeypot schemes by creating a safe environment for our investors. We "
                     "believe that a loyal community is the strongest asset in the cryptocurrency world.")
pdf.ln(10)

# Community Trust Section
pdf.set_font("Arial", "B", 14)
pdf.cell(200, 10, "Community Trust", ln=True)
pdf.set_font("Arial", "", 12)
pdf.multi_cell(0, 10, "At Polizei Doge, we prioritize the security and trust of our community. We have implemented "
                     "several mechanisms to protect our investors, including regular audits, transparency reports, "
                     "and a dedicated anti-fraud team. Our community members can count on us to remain vigilant "
                     "against malicious activities.")
pdf.ln(10)

# Transparency Section
pdf.set_font("Arial", "B", 14)
pdf.cell(200, 10, "Transparency", ln=True)
pdf.set_font("Arial", "", 12)
pdf.multi_cell(0, 10, "Transparency is key to building a loyal community. All transactions, project updates, and "
                     "community decisions are documented and available for public review. We believe that by being "
                     "open and transparent, we can build trust and ensure the longevity of Polizei Doge.")
pdf.ln(10)

# Loyalty Section
pdf.set_font("Arial", "B", 14)
pdf.cell(200, 10, "Loyalty", ln=True)
pdf.set_font("Arial", "", 12)
pdf.multi_cell(0, 10, "Polizei Doge rewards loyal community members through various incentive programs, including "
                     "loyalty rewards, exclusive events, and voting rights on important decisions. We believe that "
                     "our community is our backbone, and we are committed to supporting our loyal members.")
pdf.ln(10)

# Anti-Scam Initiatives Section
pdf.set_font("Arial", "B", 14)
pdf.cell(200, 10, "Anti-Scam Initiatives", ln=True)
pdf.set_font("Arial", "", 12)
pdf.multi_cell(0, 10, "Polizei Doge is dedicated to preventing scams and fraudulent schemes in the crypto space. Our "
                     "team actively monitors and reports suspicious activities, providing guidance to community members "
                     "on how to avoid scams. We are continuously working to create partnerships with trusted platforms "
                     "and increase our security protocols.")
pdf.ln(20)

# Closing Statement
pdf.set_font("Arial", "B", 14)
pdf.cell(200, 10, "Join Us", ln=True)
pdf.set_font("Arial", "", 12)
pdf.multi_cell(0, 10, "Join the Polizei Doge community to be part of a safe, transparent, and loyal crypto experience. "
                     "Together, we can make a positive difference in the cryptocurrency world and build a legacy based "
                     "on trust and integrity.")

# Save the file locally
pdf.output("polizei_doge_whitepaper.pdf")
