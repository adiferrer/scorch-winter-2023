# To run this code you need to run
#  pip install jinja2
# You must run this from the /jinja_files folder or else jinja can't find the templates

# 1. Import
import os
import shutil   # Used to manipulate file folders
import datetime # Used to create datetime objects to track dates and times
from jinja2 import Environment, select_autoescape, FileSystemLoader, Template
from products import products # needed for level 1 and 2

export_folder_name = "site" # Where files will be exported to

def export_all_files():
    # 2. Setup the environment
    env = Environment(autoescape=select_autoescape(), loader=FileSystemLoader("templates"))

    if os.path.exists(export_folder_name): # If a /site folder exists, delete it
        shutil.rmtree(export_folder_name)

    os.mkdir(export_folder_name) # Create directory to export to
    os.mkdir(f"{export_folder_name}{os.sep}products")

    shutil.copytree("images", f"{export_folder_name}{os.sep}images") # Copy images
    
    shutil.copyfile("templates/cart.js", f"{export_folder_name}{os.sep}cart.js")
    
    shutil.copyfile("templates/styles.css", f"{export_folder_name}{os.sep}styles.css")

    for file in os.listdir("templates"): # Go through each file in /templates
        # 3. Load a template
        if file.startswith("component") or file.startswith("base") or file.startswith("cart") or file.startswith("styles"): # Ignore some files
            continue
        example_template = env.get_template(file)

        # 4. Render template with variables
        if file =="profile.jinja":
            html = example_template.render(user={"name":"Jezika La Vye","image":"images/profile-pic.jpg", "currency":"CAD($)", "language":"english", "sign-up-date":datetime.datetime(2023,1,29), "email":"janeDoe@example.com"})
        elif file == "products.jinja":
            html = example_template.render(products=products);
        elif file == "product.jinja":
            for product in products:
                html = example_template.render(product=product);
                # Create new file path based on old file name (i.e. index.jinja would be in /site/index.html)
                new_filepath = f"{export_folder_name}{os.sep}products{os.sep}{product['name'].lower()}.html"

                with open(new_filepath, "w+", encoding="utf-8") as html_file: # Export to file
                # Store file in /site/<filename>.html 
                    html_file.write(html)
            continue
        else:
            html = example_template.render()

        # Create new file path based on old file name (i.e. index.jinja would be in /site/index.html)
        new_filepath = f"{export_folder_name}{os.sep}{file.replace('.jinja', '')}.html"

        with open(new_filepath, "w+", encoding="utf-8") as html_file: # Export to file
            # Store file in /site/<filename>.html 
            html_file.write(html)

if __name__ == "__main__": # Runs when file is run
    export_all_files()