#!/usr/bin/env python3
"""
Render Draw.io diagram to PNG with Cisco symbols.
This script parses the .drawio XML and renders it with proper Cisco icons.
"""

import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import base64
import io

# Cisco SVG symbol definitions (simplified versions)
CISCO_SYMBOLS = {
    'router': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 78 53">
        <!-- Router body -->
        <rect x="2" y="10" width="74" height="33" fill="#036897" stroke="#ffffff" stroke-width="2" rx="3"/>
        <!-- Top indicators -->
        <circle cx="15" cy="20" r="2" fill="#00ff00"/>
        <circle cx="25" cy="20" r="2" fill="#00ff00"/>
        <circle cx="35" cy="20" r="2" fill="#00ff00"/>
        <!-- Ports -->
        <rect x="10" y="28" width="8" height="10" fill="#ffffff" stroke="#036897"/>
        <rect x="25" y="28" width="8" height="10" fill="#ffffff" stroke="#036897"/>
        <rect x="40" y="28" width="8" height="10" fill="#ffffff" stroke="#036897"/>
        <rect x="55" y="28" width="8" height="10" fill="#ffffff" stroke="#036897"/>
        <!-- Front panel line -->
        <line x1="10" y1="24" x2="68" y2="24" stroke="#ffffff" stroke-width="1"/>
    </svg>''',
    
    'switch': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 101 50">
        <!-- Switch body -->
        <rect x="2" y="8" width="97" height="34" fill="#036897" stroke="#ffffff" stroke-width="2" rx="2"/>
        <!-- LED indicators -->
        <circle cx="12" cy="16" r="1.5" fill="#00ff00"/>
        <circle cx="20" cy="16" r="1.5" fill="#00ff00"/>
        <circle cx="28" cy="16" r="1.5" fill="#00ff00"/>
        <circle cx="36" cy="16" r="1.5" fill="#00ff00"/>
        <!-- Ports row 1 -->
        <rect x="10" y="24" width="6" height="8" fill="#ffffff" stroke="#036897"/>
        <rect x="18" y="24" width="6" height="8" fill="#ffffff" stroke="#036897"/>
        <rect x="26" y="24" width="6" height="8" fill="#ffffff" stroke="#036897"/>
        <rect x="34" y="24" width="6" height="8" fill="#ffffff" stroke="#036897"/>
        <rect x="42" y="24" width="6" height="8" fill="#ffffff" stroke="#036897"/>
        <rect x="50" y="24" width="6" height="8" fill="#ffffff" stroke="#036897"/>
        <rect x="58" y="24" width="6" height="8" fill="#ffffff" stroke="#036897"/>
        <rect x="66" y="24" width="6" height="8" fill="#ffffff" stroke="#036897"/>
        <rect x="74" y="24" width="6" height="8" fill="#ffffff" stroke="#036897"/>
        <rect x="82" y="24" width="6" height="8" fill="#ffffff" stroke="#036897"/>
    </svg>''',
    
    'pc': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 36">
        <!-- Monitor -->
        <rect x="4" y="2" width="32" height="22" fill="#036897" stroke="#ffffff" stroke-width="2" rx="2"/>
        <rect x="7" y="5" width="26" height="16" fill="#ffffff" stroke="#036897"/>
        <!-- Stand -->
        <rect x="17" y="24" width="6" height="4" fill="#036897"/>
        <!-- Base -->
        <rect x="10" y="28" width="20" height="6" fill="#036897" stroke="#ffffff" stroke-width="1" rx="2"/>
    </svg>'''
}

def parse_style(style_str):
    """Parse style string into a dictionary."""
    if not style_str:
        return {}
    style = {}
    for part in style_str.split(';'):
        if '=' in part:
            key, value = part.split('=', 1)
            style[key.strip()] = value.strip()
    return style

def get_cisco_icon(shape_name):
    """Get the appropriate Cisco icon based on shape name."""
    if 'router' in shape_name.lower():
        return 'router'
    elif 'switch' in shape_name.lower():
        return 'switch'
    elif 'pc' in shape_name.lower() or 'computer' in shape_name.lower():
        return 'pc'
    return None

def render_cisco_symbol(draw, x, y, width, height, symbol_type, color='#036897'):
    """Render a Cisco symbol on the image."""
    # For now, we'll render simple representations
    # In a production version, we would render the SVG properly
    
    if symbol_type == 'router':
        # Draw router box
        draw.rectangle([x, y, x+width, y+height], fill=color, outline='white', width=2)
        # Draw LEDs
        led_y = y + height//4
        for i in range(3):
            led_x = x + (i+1) * width//4
            draw.ellipse([led_x-3, led_y-3, led_x+3, led_y+3], fill='#00ff00')
        # Draw ports
        port_y = y + height//2
        for i in range(4):
            port_x = x + (i+1) * width//5
            draw.rectangle([port_x-4, port_y, port_x+4, port_y+height//3], 
                         fill='white', outline=color, width=1)
    
    elif symbol_type == 'switch':
        # Draw switch box
        draw.rectangle([x, y, x+width, y+height], fill=color, outline='white', width=2)
        # Draw LEDs
        led_y = y + height//4
        for i in range(4):
            led_x = x + (i+1) * width//5
            draw.ellipse([led_x-2, led_y-2, led_x+2, led_y+2], fill='#00ff00')
        # Draw many ports
        port_y = y + height//2
        num_ports = 10
        port_spacing = width // (num_ports + 1)
        for i in range(num_ports):
            port_x = x + (i+1) * port_spacing
            draw.rectangle([port_x-3, port_y, port_x+3, port_y+height//3], 
                         fill='white', outline=color, width=1)
    
    elif symbol_type == 'pc':
        # Draw monitor
        monitor_height = int(height * 0.6)
        draw.rectangle([x, y, x+width, y+monitor_height], fill=color, outline='white', width=2)
        # Draw screen
        screen_margin = 4
        draw.rectangle([x+screen_margin, y+screen_margin, 
                       x+width-screen_margin, y+monitor_height-screen_margin], 
                      fill='white', outline=color)
        # Draw stand
        stand_width = width // 3
        stand_x = x + width//2 - stand_width//2
        stand_y = y + monitor_height
        draw.rectangle([stand_x, stand_y, stand_x+stand_width, stand_y+height//10], fill=color)
        # Draw base
        base_width = int(width * 0.8)
        base_x = x + width//2 - base_width//2
        base_y = y + monitor_height + height//10
        draw.rectangle([base_x, base_y, base_x+base_width, y+height], 
                      fill=color, outline='white', width=1)

def export_drawio_to_png(drawio_path, png_path):
    """Export Draw.io diagram to PNG with Cisco symbols."""
    drawio_path = Path(drawio_path)
    png_path = Path(png_path)
    
    if not drawio_path.exists():
        print(f"Error: {drawio_path} does not exist")
        return False
    
    # Parse the Draw.io XML
    tree = ET.parse(drawio_path)
    root = tree.getroot()
    
    # Find the diagram element
    diagram = root.find('.//diagram')
    if diagram is None:
        print("Error: No diagram found in file")
        return False
    
    # Get the mxGraphModel
    model = diagram.find('.//mxGraphModel')
    if model is None:
        print("Error: No mxGraphModel found")
        return False
    
    # Get dimensions from model
    width = int(model.get('pageWidth', '1169'))
    height = int(model.get('pageHeight', '827'))
    
    # Create image with white background
    img = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(img)
    
    # Try to load a font
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 12)
        font_bold = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 12)
    except:
        font = ImageFont.load_default()
        font_bold = font
    
    # Parse all cells
    cells = {}
    for cell in model.findall('.//mxCell'):
        cell_id = cell.get('id')
        cells[cell_id] = cell
    
    # First pass: render rectangles and shapes
    for cell in model.findall('.//mxCell'):
        cell_id = cell.get('id')
        style = parse_style(cell.get('style', ''))
        value = cell.get('value', '')
        
        # Get geometry
        geom = cell.find('mxGeometry')
        if geom is None:
            continue
        
        x = float(geom.get('x', '0'))
        y = float(geom.get('y', '0'))
        w = float(geom.get('width', '100'))
        h = float(geom.get('height', '50'))
        
        # Check if it's a Cisco shape
        shape = style.get('shape', '')
        icon_type = get_cisco_icon(shape)
        
        if icon_type:
            # Render Cisco symbol
            color = style.get('fillColor', '#036897')
            render_cisco_symbol(draw, int(x), int(y), int(w), int(h), icon_type, color)
        
        elif 'whiteSpace=wrap' in style.get('shape', '') or 'rounded' in style.get('shape', ''):
            # Render box/rectangle (like VLAN legend)
            fill_color = style.get('fillColor', '#dae8fc')
            stroke_color = style.get('strokeColor', '#6c8ebf')
            
            # Convert hex colors to RGB tuples
            def hex_to_rgb(hex_color):
                hex_color = hex_color.lstrip('#')
                return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
            
            try:
                fill_rgb = hex_to_rgb(fill_color)
                stroke_rgb = hex_to_rgb(stroke_color)
                draw.rectangle([x, y, x+w, y+h], fill=fill_rgb, outline=stroke_rgb, width=2)
            except:
                draw.rectangle([x, y, x+w, y+h], fill='lightblue', outline='blue', width=2)
    
    # Second pass: render connections/edges
    for cell in model.findall('.//mxCell'):
        style = parse_style(cell.get('style', ''))
        
        # Check if it's an edge
        if cell.get('edge') == '1':
            source_id = cell.get('source')
            target_id = cell.get('target')
            
            if source_id in cells and target_id in cells:
                source_geom = cells[source_id].find('mxGeometry')
                target_geom = cells[target_id].find('mxGeometry')
                
                if source_geom is not None and target_geom is not None:
                    sx = float(source_geom.get('x', '0')) + float(source_geom.get('width', '0'))/2
                    sy = float(source_geom.get('y', '0')) + float(source_geom.get('height', '0'))
                    tx = float(target_geom.get('x', '0')) + float(target_geom.get('width', '0'))/2
                    ty = float(target_geom.get('y', '0'))
                    
                    stroke_color = style.get('strokeColor', '#000000')
                    stroke_width = int(style.get('strokeWidth', '2'))
                    
                    # Draw line
                    draw.line([(sx, sy), (tx, ty)], fill='black', width=stroke_width)
    
    # Third pass: render text labels
    for cell in model.findall('.//mxCell'):
        value = cell.get('value', '')
        if not value:
            continue
        
        geom = cell.find('mxGeometry')
        if geom is None:
            continue
        
        x = float(geom.get('x', '0'))
        y = float(geom.get('y', '0'))
        w = float(geom.get('width', '100'))
        h = float(geom.get('height', '50'))
        
        style = parse_style(cell.get('style', ''))
        
        # Clean up value (remove HTML tags)
        value = value.replace('&#xa;', '\n')
        
        # Determine if this is a label below/above a shape
        is_vertex = cell.get('vertex') == '1'
        
        # Draw text
        lines = value.split('\n')
        font_height = 14
        total_height = len(lines) * font_height
        
        # Center text in the cell
        text_y = y + (h - total_height) / 2
        
        for i, line in enumerate(lines):
            if line.strip():
                # Get text bounding box
                bbox = draw.textbbox((0, 0), line, font=font)
                text_width = bbox[2] - bbox[0]
                text_x = x + (w - text_width) / 2
                
                # Draw text with outline for better visibility
                outline_color = 'white'
                text_color = 'black'
                
                # Draw outline
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx != 0 or dy != 0:
                            draw.text((text_x+dx, text_y+dy+i*font_height), line, 
                                    fill=outline_color, font=font)
                
                # Draw main text
                draw.text((text_x, text_y+i*font_height), line, fill=text_color, font=font_bold)
    
    # Save the image
    img.save(png_path, 'PNG')
    print(f"Successfully exported to {png_path}")
    print(f"Image size: {width}x{height}")
    
    return True

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: render_diagram.py <input.drawio> <output.png>")
        sys.exit(1)
    
    drawio_file = sys.argv[1]
    png_file = sys.argv[2]
    
    success = export_drawio_to_png(drawio_file, png_file)
    sys.exit(0 if success else 1)
