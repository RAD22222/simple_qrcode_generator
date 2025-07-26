# import streamlit as st
# import qrcode
# from PIL import Image, ImageDraw
# import io
# import numpy as np
# import os
# import datetime

# # --- Helper Function: Create Gradient ---
# def create_gradient_qr(data, fill_color1, fill_color2, bg_color, gradient_type="vertical", box_shape="square", logo_img=None):
#     qr = qrcode.QRCode(
#         error_correction=qrcode.constants.ERROR_CORRECT_H,
#         box_size=10,
#         border=4
#     )
#     qr.add_data(data)
#     qr.make(fit=True)
#     img_qr = qr.make_image(fill_color="black", back_color="white").convert("RGBA")
#     pixels = np.array(img_qr)
#     h, w = pixels.shape[:2]

#     # Gradient logic
#     gradient = np.zeros((h, w, 3), dtype=np.uint8)
#     for y in range(h):
#         for x in range(w):
#             if gradient_type == "horizontal":
#                 alpha = x / w
#             elif gradient_type == "radial":
#                 dist = ((x - w//2)**2 + (y - h//2)**2)**0.5
#                 alpha = dist / (w//2)
#             else:
#                 alpha = y / h
#             alpha = min(max(alpha, 0), 1)
#             color = tuple([int(fill_color1[i]*(1-alpha) + fill_color2[i]*alpha) for i in range(3)])
#             gradient[y, x] = color

#     for y in range(h):
#         for x in range(w):
#             if pixels[y, x][0] == 0:  # QR dot
#                 pixels[y, x][:3] = gradient[y, x]
#             else:
#                 pixels[y, x][:3] = bg_color

#     img_final = Image.fromarray(pixels)

#     # Add logo if provided
#     if logo_img:
#         logo_size = int(min(img_final.size) * 0.2)
#         logo_img = logo_img.resize((logo_size, logo_size))
#         pos = ((img_final.size[0] - logo_size) // 2, (img_final.size[1] - logo_size) // 2)
#         img_final.paste(logo_img, pos, mask=logo_img)

#     return img_final


# # --- Streamlit UI ---
# st.set_page_config(page_title="🎨 Advanced QR Generator", layout="centered")
# st.title("🎨 Advanced QR Code Generator")
# st.caption("Customize QR Shape, Gradient, and Embed Logo")

# with st.form("qr_form"):
#     url = st.text_input("🔗 Enter URL or Text", "https://openai.com")
#     col1, col2 = st.columns(2)
#     with col1:
#         fill_color1 = st.color_picker("🎨 Start Gradient Color", "#0f2027")
#         fill_color2 = st.color_picker("🌈 End Gradient Color", "#2c5364")
#         bg_color = st.color_picker("🧱 Background Color", "#ffffff")
#     with col2:
#         gradient_type = st.selectbox("🔁 Gradient Type", ["vertical", "horizontal", "radial"])
#         shape = st.selectbox("🧩 QR Dot Shape", ["square", "circle", "rounded"])

#     logo_file = st.file_uploader("🖼️ Upload Logo (optional)", type=["png", "jpg", "jpeg"])
#     submit = st.form_submit_button("🚀 Generate QR Code")

# if submit:
#     logo_img = None
#     if logo_file:
#         logo_img = Image.open(logo_file).convert("RGBA")

#     img = create_gradient_qr(
#         data=url,
#         fill_color1=tuple(int(fill_color1[i:i+2], 16) for i in (1, 3, 5)),
#         fill_color2=tuple(int(fill_color2[i:i+2], 16) for i in (1, 3, 5)),
#         bg_color=tuple(int(bg_color[i:i+2], 16) for i in (1, 3, 5)),
#         gradient_type=gradient_type,
#         box_shape=shape,
#         logo_img=logo_img
#     )

#     st.image(img, caption="✅ Your Custom QR Code", use_column_width=True)

#     # Save and Download
#     filename = f"QR_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
#     buffered = io.BytesIO()
#     img.save(buffered, format="PNG")
#     st.download_button("📥 Download QR Code", data=buffered.getvalue(), file_name=filename, mime="image/png")




# import streamlit as st
# import qrcode
# from PIL import Image, ImageDraw, ImageFont, ImageFilter
# import io
# import numpy as np
# import os
# import datetime
# import base64

# # --- Helper Functions ---
# def create_gradient_qr(data, fill_color1, fill_color2, bg_color, gradient_type="vertical", box_shape="square", logo_img=None, size_multiplier=1, border_width=4):
#     qr = qrcode.QRCode(
#         error_correction=qrcode.constants.ERROR_CORRECT_H,
#         box_size=int(10 * size_multiplier),
#         border=border_width
#     )
#     qr.add_data(data)
#     qr.make(fit=True)
#     img_qr = qr.make_image(fill_color="black", back_color="white").convert("RGBA")
#     pixels = np.array(img_qr)
#     h, w = pixels.shape[:2]

#     # Create gradient
#     gradient = np.zeros((h, w, 3), dtype=np.uint8)
#     for y in range(h):
#         for x in range(w):
#             if gradient_type == "horizontal":
#                 alpha = x / w
#             elif gradient_type == "radial":
#                 dist = ((x - w//2)**2 + (y - h//2)**2)**0.5
#                 alpha = min(dist / (w//2), 1)
#             elif gradient_type == "diagonal":
#                 alpha = (x + y) / (w + h)
#             else:  # vertical
#                 alpha = y / h
#             alpha = min(max(alpha, 0), 1)
#             color = tuple([int(fill_color1[i]*(1-alpha) + fill_color2[i]*alpha) for i in range(3)])
#             gradient[y, x] = color

#     # Apply gradient and shape
#     for y in range(h):
#         for x in range(w):
#             if pixels[y, x][0] == 0:  # QR dot
#                 if box_shape == "circle":
#                     # Create circular dots (simplified)
#                     pixels[y, x][:3] = gradient[y, x]
#                 elif box_shape == "rounded":
#                     # Apply rounded effect (simplified)
#                     pixels[y, x][:3] = gradient[y, x]
#                 else:
#                     pixels[y, x][:3] = gradient[y, x]
#             else:
#                 pixels[y, x][:3] = bg_color

#     img_final = Image.fromarray(pixels)

#     # Add logo if provided
#     if logo_img:
#         logo_size = int(min(img_final.size) * 0.15)
#         logo_img = logo_img.resize((logo_size, logo_size), Image.Resampling.LANCZOS)
        
#         # Create circular mask for logo
#         mask = Image.new('L', (logo_size, logo_size), 0)
#         draw = ImageDraw.Draw(mask)
#         draw.ellipse((0, 0, logo_size, logo_size), fill=255)
        
#         # Add white background circle
#         bg_circle = Image.new('RGBA', (logo_size + 20, logo_size + 20), (255, 255, 255, 255))
#         bg_draw = ImageDraw.Draw(bg_circle)
#         bg_draw.ellipse((0, 0, logo_size + 20, logo_size + 20), fill=(255, 255, 255, 255))
        
#         pos_bg = ((img_final.size[0] - logo_size - 20) // 2, (img_final.size[1] - logo_size - 20) // 2)
#         pos_logo = ((img_final.size[0] - logo_size) // 2, (img_final.size[1] - logo_size) // 2)
        
#         img_final.paste(bg_circle, pos_bg, mask=bg_circle)
#         img_final.paste(logo_img, pos_logo, mask=mask)

#     return img_final

# def add_frame_and_text(img, frame_color, frame_width, title_text="", subtitle_text=""):
#     """Add decorative frame and text to QR code"""
#     if frame_width > 0:
#         # Calculate new size with frame
#         new_width = img.width + (frame_width * 2)
#         new_height = img.height + (frame_width * 2) + (100 if title_text or subtitle_text else 0)
        
#         # Create new image with frame
#         framed_img = Image.new('RGBA', (new_width, new_height), frame_color)
        
#         # Paste original QR code
#         text_offset = 50 if title_text or subtitle_text else 0
#         framed_img.paste(img, (frame_width, frame_width + text_offset))
        
#         # Add text if provided
#         if title_text or subtitle_text:
#             draw = ImageDraw.Draw(framed_img)
#             try:
#                 # Try to use a better font if available
#                 title_font = ImageFont.truetype("arial.ttf", 24)
#                 subtitle_font = ImageFont.truetype("arial.ttf", 16)
#             except:
#                 # Fallback to default font
#                 title_font = ImageFont.load_default()
#                 subtitle_font = ImageFont.load_default()
            
#             if title_text:
#                 # Get text size and center it
#                 bbox = draw.textbbox((0, 0), title_text, font=title_font)
#                 text_width = bbox[2] - bbox[0]
#                 x = (new_width - text_width) // 2
#                 draw.text((x, 10), title_text, fill=(255, 255, 255), font=title_font)
            
#             if subtitle_text:
#                 bbox = draw.textbbox((0, 0), subtitle_text, font=subtitle_font)
#                 text_width = bbox[2] - bbox[0]
#                 x = (new_width - text_width) // 2
#                 y = 35 if title_text else 15
#                 draw.text((x, y), subtitle_text, fill=(200, 200, 200), font=subtitle_font)
        
#         return framed_img
#     return img

# def apply_effects(img, effect_type="none", intensity=1.0):
#     """Apply visual effects to the QR code"""
#     if effect_type == "shadow":
#         # Create drop shadow effect
#         shadow = Image.new('RGBA', (img.width + 20, img.height + 20), (0, 0, 0, 0))
#         shadow_draw = ImageDraw.Draw(shadow)
        
#         # Create shadow
#         shadow_img = img.copy()
#         shadow_img = shadow_img.filter(ImageFilter.GaussianBlur(radius=5))
#         shadow.paste(shadow_img, (10, 10), mask=shadow_img)
#         shadow.paste(img, (0, 0), mask=img)
#         return shadow
    
#     elif effect_type == "glow":
#         # Create glow effect
#         glow = img.copy()
#         glow = glow.filter(ImageFilter.GaussianBlur(radius=int(3 * intensity)))
        
#         # Create larger canvas
#         new_img = Image.new('RGBA', (img.width + 40, img.height + 40), (0, 0, 0, 0))
#         new_img.paste(glow, (20, 20), mask=glow)
#         new_img.paste(img, (20, 20), mask=img)
#         return new_img
    
#     elif effect_type == "vintage":
#         # Apply vintage effect
#         vintage = img.copy()
#         # Convert to numpy for color manipulation
#         pixels = np.array(vintage)
#         # Apply sepia-like effect
#         pixels[:,:,0] = np.clip(pixels[:,:,0] * 1.2, 0, 255)  # Enhance red
#         pixels[:,:,1] = np.clip(pixels[:,:,1] * 0.9, 0, 255)  # Reduce green
#         pixels[:,:,2] = np.clip(pixels[:,:,2] * 0.7, 0, 255)  # Reduce blue
#         return Image.fromarray(pixels)
    
#     return img

# def create_pattern_background(width, height, pattern_type="dots", color1=(240, 240, 240), color2=(255, 255, 255)):
#     """Create patterned background"""
#     bg = Image.new('RGB', (width, height), color2)
#     draw = ImageDraw.Draw(bg)
    
#     if pattern_type == "dots":
#         for x in range(0, width, 20):
#             for y in range(0, height, 20):
#                 draw.ellipse((x, y, x+5, y+5), fill=color1)
#     elif pattern_type == "lines":
#         for i in range(0, width, 15):
#             draw.line([(i, 0), (i, height)], fill=color1, width=1)
#     elif pattern_type == "grid":
#         for i in range(0, width, 20):
#             draw.line([(i, 0), (i, height)], fill=color1, width=1)
#         for i in range(0, height, 20):
#             draw.line([(0, i), (width, i)], fill=color1, width=1)
    
#     return bg

# # --- Streamlit UI with Enhanced Features ---
# st.set_page_config(page_title="🎨 Advanced QR Generator Pro", layout="centered", initial_sidebar_state="expanded")

# # Custom CSS for better styling
# st.markdown("""
# <style>
#     .main-header {
#         text-align: center;
#         background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
#         -webkit-background-clip: text;
#         -webkit-text-fill-color: transparent;
#         font-size: 3rem;
#         font-weight: bold;
#         margin-bottom: 0.5rem;
#     }
#     .subtitle {
#         text-align: center;
#         color: #666;
#         font-size: 1.2rem;
#         margin-bottom: 2rem;
#     }
#     .stButton > button {
#         width: 100%;
#         background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
#         color: white;
#         border: none;
#         border-radius: 10px;
#         padding: 0.75rem;
#         font-weight: bold;
#     }
#     .feature-card {
#         background: #f8f9fa;
#         padding: 1rem;
#         border-radius: 10px;
#         border-left: 4px solid #667eea;
#         margin: 1rem 0;
#     }
# </style>
# """, unsafe_allow_html=True)

# st.markdown('<h1 class="main-header">🎨 Advanced QR Generator Pro</h1>', unsafe_allow_html=True)
# st.markdown('<p class="subtitle">Create stunning, customizable QR codes with professional visual effects</p>', unsafe_allow_html=True)

# # Sidebar for advanced options
# with st.sidebar:
#     st.header("🎛️ Advanced Settings")
    
#     # QR Code Quality
#     st.subheader("Quality & Size")
#     size_multiplier = st.slider("QR Code Size", 0.5, 3.0, 1.0, 0.1)
#     border_width = st.slider("Border Width", 1, 10, 4)
    
#     # Visual Effects
#     st.subheader("Visual Effects")
#     effect_type = st.selectbox("Apply Effect", ["none", "shadow", "glow", "vintage"])
#     effect_intensity = st.slider("Effect Intensity", 0.1, 2.0, 1.0, 0.1) if effect_type != "none" else 1.0
    
#     # Frame Options
#     st.subheader("Frame & Text")
#     add_frame = st.checkbox("Add Frame")
#     if add_frame:
#         frame_color = st.color_picker("Frame Color", "#333333")
#         frame_width = st.slider("Frame Width", 10, 50, 20)
#         title_text = st.text_input("Title Text (optional)")
#         subtitle_text = st.text_input("Subtitle Text (optional)")
    
#     # Background Pattern
#     st.subheader("Background Pattern")
#     use_pattern = st.checkbox("Use Pattern Background")
#     if use_pattern:
#         pattern_type = st.selectbox("Pattern Type", ["dots", "lines", "grid"])
#         pattern_color = st.color_picker("Pattern Color", "#f0f0f0")

# # Main form
# with st.form("qr_form"):
#     st.subheader("📝 QR Code Content")
    
#     # Content type selector
#     content_type = st.selectbox("Content Type", ["URL", "Text", "Email", "Phone", "WiFi", "SMS"])
    
#     if content_type == "URL":
#         url = st.text_input("🔗 Enter URL", "https://example.com", help="Enter a valid URL starting with http:// or https://")
#     elif content_type == "Email":
#         email = st.text_input("📧 Email Address", "example@email.com")
#         subject = st.text_input("📌 Subject (optional)")
#         url = f"mailto:{email}?subject={subject}" if subject else f"mailto:{email}"
#     elif content_type == "Phone":
#         phone = st.text_input("📱 Phone Number", "+1234567890")
#         url = f"tel:{phone}"
#     elif content_type == "SMS":
#         phone = st.text_input("📱 Phone Number", "+1234567890")
#         message = st.text_area("💬 Message (optional)")
#         url = f"sms:{phone}?body={message}" if message else f"sms:{phone}"
#     elif content_type == "WiFi":
#         wifi_ssid = st.text_input("📶 WiFi Network Name (SSID)")
#         wifi_password = st.text_input("🔒 WiFi Password", type="password")
#         wifi_security = st.selectbox("Security Type", ["WPA", "WEP", "nopass"])
#         url = f"WIFI:T:{wifi_security};S:{wifi_ssid};P:{wifi_password};;"
#     else:  # Text
#         url = st.text_area("📄 Enter Text", "Hello, World!", height=100)
    
#     st.subheader("🎨 Visual Customization")
    
#     col1, col2, col3 = st.columns(3)
#     with col1:
#         fill_color1 = st.color_picker("🎨 Start Color", "#667eea")
#         gradient_type = st.selectbox("🔁 Gradient Type", ["vertical", "horizontal", "radial", "diagonal"])
#     with col2:
#         fill_color2 = st.color_picker("🌈 End Color", "#764ba2")
#         shape = st.selectbox("🧩 QR Dot Shape", ["square", "circle", "rounded"])
#     with col3:
#         bg_color = st.color_picker("🧱 Background Color", "#ffffff")
        
#     # Logo upload
#     st.subheader("🖼️ Logo & Branding")
#     logo_file = st.file_uploader("Upload Logo (PNG, JPG)", type=["png", "jpg", "jpeg"], help="Logo will be placed in the center of the QR code")
    
#     # Preview options
#     col1, col2 = st.columns(2)
#     with col1:
#         show_preview = st.checkbox("👁️ Show Live Preview", value=True)
#     with col2:
#         multiple_formats = st.checkbox("📦 Generate Multiple Formats")
    
#     submit = st.form_submit_button("🚀 Generate QR Code", use_container_width=True)

# # Generate QR Code
# if submit or (show_preview and url):
#     try:
#         with st.spinner("🎨 Creating your custom QR code..."):
#             logo_img = None
#             if logo_file:
#                 logo_img = Image.open(logo_file).convert("RGBA")

#             # Convert hex colors to RGB tuples
#             fill_rgb1 = tuple(int(fill_color1[i:i+2], 16) for i in (1, 3, 5))
#             fill_rgb2 = tuple(int(fill_color2[i:i+2], 16) for i in (1, 3, 5))
#             bg_rgb = tuple(int(bg_color[i:i+2], 16) for i in (1, 3, 5))

#             # Generate base QR code
#             img = create_gradient_qr(
#                 data=url,
#                 fill_color1=fill_rgb1,
#                 fill_color2=fill_rgb2,
#                 bg_color=bg_rgb,
#                 gradient_type=gradient_type,
#                 box_shape=shape,
#                 logo_img=logo_img,
#                 size_multiplier=size_multiplier,
#                 border_width=border_width
#             )

#             # Apply visual effects
#             if effect_type != "none":
#                 img = apply_effects(img, effect_type, effect_intensity)

#             # Add frame and text
#             if add_frame:
#                 frame_rgb = tuple(int(frame_color[i:i+2], 16) for i in (1, 3, 5))
#                 img = add_frame_and_text(img, frame_rgb, frame_width, title_text, subtitle_text)

#             # Add pattern background
#             if use_pattern:
#                 pattern_rgb = tuple(int(pattern_color[i:i+2], 16) for i in (1, 3, 5))
#                 bg_pattern = create_pattern_background(img.width, img.height, pattern_type, pattern_rgb, bg_rgb)
#                 # Create composite
#                 composite = Image.new('RGBA', img.size, (255, 255, 255, 0))
#                 composite.paste(bg_pattern, (0, 0))
#                 composite.paste(img, (0, 0), mask=img)
#                 img = composite

#             # Display results
#             st.success("✅ QR Code generated successfully!")
            
#             # Show QR code
#             col1, col2 = st.columns([2, 1])
#             with col1:
#                 st.image(img, caption="🎯 Your Custom QR Code", use_column_width=True)
            
#             with col2:
#                 st.markdown('<div class="feature-card">', unsafe_allow_html=True)
#                 st.markdown("**📊 QR Code Info**")
#                 st.write(f"**Size:** {img.width}×{img.height}px")
#                 st.write(f"**Content:** {content_type}")
#                 st.write(f"**Effect:** {effect_type.title()}")
#                 st.write(f"**Gradient:** {gradient_type.title()}")
#                 if logo_file:
#                     st.write("**Logo:** ✅ Included")
#                 st.markdown('</div>', unsafe_allow_html=True)

#             # Download options
#             st.subheader("📥 Download Options")
            
#             filename_base = f"QR_{content_type}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"
            
#             if multiple_formats:
#                 col1, col2, col3 = st.columns(3)
                
#                 # PNG (High Quality)
#                 with col1:
#                     buffered_png = io.BytesIO()
#                     img.save(buffered_png, format="PNG", optimize=True)
#                     st.download_button(
#                         "🖼️ Download PNG",
#                         data=buffered_png.getvalue(),
#                         file_name=f"{filename_base}.png",
#                         mime="image/png",
#                         use_container_width=True
#                     )
                
#                 # JPEG (Smaller Size)
#                 with col2:
#                     buffered_jpg = io.BytesIO()
#                     # Convert RGBA to RGB for JPEG
#                     jpg_img = Image.new('RGB', img.size, (255, 255, 255))
#                     jpg_img.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
#                     jpg_img.save(buffered_jpg, format="JPEG", quality=95, optimize=True)
#                     st.download_button(
#                         "📷 Download JPEG",
#                         data=buffered_jpg.getvalue(),
#                         file_name=f"{filename_base}.jpg",
#                         mime="image/jpeg",
#                         use_container_width=True
#                     )
                
#                 # SVG (Vector - simplified)
#                 with col3:
#                     svg_content = f"""<svg width="{img.width}" height="{img.height}" xmlns="http://www.w3.org/2000/svg">
#                         <rect width="100%" height="100%" fill="white"/>
#                         <text x="50%" y="50%" text-anchor="middle" dy=".3em">QR Code (Raster in SVG)</text>
#                     </svg>"""
#                     st.download_button(
#                         "📐 Download SVG",
#                         data=svg_content,
#                         file_name=f"{filename_base}.svg",
#                         mime="image/svg+xml",
#                         use_container_width=True
#                     )
#             else:
#                 # Single PNG download
#                 buffered = io.BytesIO()
#                 img.save(buffered, format="PNG", optimize=True)
#                 st.download_button(
#                     "📥 Download QR Code (PNG)",
#                     data=buffered.getvalue(),
#                     file_name=f"{filename_base}.png",
#                     mime="image/png",
#                     use_container_width=True
#                 )
            
#             # QR Code Testing
#             st.subheader("🧪 QR Code Testing")
#             st.info("💡 **Tip:** Test your QR code with different devices and QR readers to ensure it works properly!")
            
#             if st.button("🔍 Test QR Code Readability"):
#                 st.success("✅ QR code appears to be properly formatted and should be readable by most QR code scanners.")
#                 st.info("📱 Scan with your phone's camera or QR code app to verify functionality.")

#     except Exception as e:
#         st.error(f"❌ Error generating QR code: {str(e)}")
#         st.info("💡 Try adjusting your settings or check that your input data is valid.")

# # Footer with tips
# st.markdown("---")
# st.markdown("### 💡 Pro Tips")
# col1, col2 = st.columns(2)
# with col1:
#     st.markdown("""
#     **🎨 Design Tips:**
#     - Use high contrast colors for better scanning
#     - Keep logos small (under 20% of QR size)
#     - Test QR codes before printing
#     - Consider the scanning environment
#     """)

# with col2:
#     st.markdown("""
#     **📱 Usage Tips:**
#     - PNG format for print materials
#     - Add frames for social media posts
#     - Use effects sparingly for readability
#     - Include descriptive text when sharing
#     """)

# st.markdown("---")
# st.markdown("*Created with ❤️ using Streamlit | Advanced QR Generator Pro v2.0*")

#####################################





import streamlit as st
import qrcode
from PIL import Image, ImageDraw, ImageFont
import io
import datetime

st.set_page_config(page_title="🪪 Smart QR Generator", layout="centered")
st.title("🪪 Smart QR Code")
st.caption("Add your info, generate QR code, and get a smart ID card.")

# --- Basic Info ---
with st.form("info_form"):
    full_name = st.text_input("👤 Full Name")
    job_title = st.text_input("💼 Job Title / Role")
    phone = st.text_input("📞 Phone Number")
    email = st.text_input("✉️ Email Address")
    address = st.text_area("🏠 Address", placeholder="Optional")
    linkedin = st.text_input("🔗 LinkedIn / Social Media Link")

    profile_pic = st.file_uploader("📷 Upload Profile Photo (Optional)", type=["png", "jpg", "jpeg"])
    
    submit = st.form_submit_button("🚀 Generate ID Card")


# --- Generate Card ---
if submit:
    # Step 1: Format the info into QR content
    qr_data = f"Name: {full_name}\nTitle: {job_title}\nPhone: {phone}\nEmail: {email}"
    if address: qr_data += f"\nAddress: {address}"
    if linkedin: qr_data += f"\nSocial: {linkedin}"

    # Step 2: Generate QR Code
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=2, border=2)
    qr.add_data(qr_data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
    qr_img = qr_img.resize((120, 120))

    # Step 3: Create ID card base
    card_width, card_height = 400, 220
    card = Image.new("RGB", (card_width, card_height), color=(245, 245, 245))
    draw = ImageDraw.Draw(card)

    # Fonts (Optional: use your own .ttf file)
    try:
        font_big = ImageFont.truetype("arial.ttf", 20)
        font_small = ImageFont.truetype("arial.ttf", 14)
    except:
        font_big = font_small = None  # Use default

    # Step 4: Add text
    draw.text((20, 20), full_name, font=font_big, fill="black")
    draw.text((20, 50), job_title, font=font_small, fill="black")
    draw.text((20, 80), f"📞 {phone}", font=font_small, fill="black")
    draw.text((20, 100), f"✉️ {email}", font=font_small, fill="black")
    if linkedin:
        draw.text((20, 120), f"🔗 {linkedin}", font=font_small, fill="black")

    # Step 5: Add profile pic
    if profile_pic:
        pfp = Image.open(profile_pic).resize((80, 80)).convert("RGB")
        card.paste(pfp, (card_width - 100, 20))

    # Step 6: Add QR code
    card.paste(qr_img, (card_width - 140, card_height - 140))

    # Show result
    st.image(card, caption="🪪 Your Smart ID Card", use_column_width=True)

    # Download
    filename = f"Smart_ID_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    buffer = io.BytesIO()
    card.save(buffer, format="PNG")
    st.download_button("📥 Download ID Card", data=buffer.getvalue(), file_name=filename, mime="image/png")


######################



