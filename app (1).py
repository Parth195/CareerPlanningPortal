from flask import Flask, request, render_template, redirect, url_for
import pathlib
import textwrap
import google.generativeai as genai
from IPython.display import Markdown
from IPython.display import display

app = Flask(__name__)

def to_html(text):
    return text.data

# Configure Google API key
GOOGLE_API_KEY = 'AIzaSyD9yEVJWCnhUxvuocCPXlfHxoHtqHZ4K6M'
genai.configure(api_key=GOOGLE_API_KEY)

# Load the GenerativeModel
model = genai.GenerativeModel('gemini-pro')
# extraction
@app.route('/colleges')
def colleges():
    # Render the HTML template for the 'colleges' page
    return render_template('colleges.html')

@app.route('/companies')
def companies():
    # Render the HTML template for the 'companies' page
    return render_template('companies.html')

@app.route('/resources')
def resources():
    # Render the HTML template for the 'resources' page
    return render_template('resources.html')

@app.route('/account')
def account():
    # Render the HTML template for the 'account' page
    return render_template('account.html')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        
        cgpa = request.form['cgpa']
        branch = request.form.get('branch')        
        specialisation = request.form.get('specialisation')
        minor = request.form.get('minor')
        internships = request.form.get('internships')
        projects = request.form.get('projects')
        
        # Extracting course grades based on branch
        if branch == 'CSE':
            dsa_grade = request.form.get('dsa')
            oops_grade = request.form.get('oops')
            daa_grade = request.form.get('daa')
            intro_to_c_grade = request.form.get('intro-to-c')
            cn_grade = request.form.get('cn')
            #added prompt
            input_text = f"My CGPA is {cgpa}, I am from {branch} branch, I have scored {dsa_grade} in Data Structures and Algorithms,{oops_grade} in Object Oriented Programming,{daa_grade} in Design and Analysis of Algorithms,{intro_to_c_grade} in Introduction to C programming and {cn_grade} in Computer Networks, I have done my specialisation in {specialisation}, I have done my minor in {minor}, I have done {internships} internships and {projects} projects should I persue Higher Education or Job?"

        elif branch == 'ECE':
            # Extract grades for ECE courses
            de_grade = request.form.get('Digital electronics')
            vlsi_grade = request.form.get('VLSI')
            emb_grade = request.form.get('Embedded system')
            dc_grade = request.form.get('Digital communication')
            sns_grade = request.form.get('Signal and system')
            #hello
            input_text = f"My CGPA is {cgpa}, I am from {branch} branch, I have scored {de_grade} in Digital Electronics,{vlsi_grade} in VLSI,{emb_grade} in Embedded system,{dc_grade} in Digital communication and {sns_grade} in Signal and system, I have done my specialisation in {specialisation}, I have done my minor in {minor}, I have done {internships} internships and {projects} projects should I persue Higher Education or Job?"

        elif branch == 'Chemical':
            # Extract grades for Chemical courses
            cp_grade = request.form.get('Chemical Principles')
            basic_oc_grade = request.form.get('Basic Organic chemistry')
            mol_mod_grade = request.form.get('Molecular modelling')
            ic_grade = request.form.get('Inorganic chemistry')
            mat_grade = request.form.get('Material Science')
            input_text = f"My CGPA is {cgpa}, I am from {branch} branch, I have scored {cp_grade} in Chemical Principles,{basic_oc_grade} in Basic Organic chemistry,{mol_mod_grade} in Molecular modelling,{ic_grade} in Inorganic chemistry and {mat_grade} in Material Science, I have done my specialisation in {specialisation}, I have done my minor in {minor}, I have done {internships} internships and {projects} projects should I persue Higher Education or Job?"

        elif branch == 'Mechanical':
            # Extract grades for Mechanical courses
            man_sci_eng_grade = request.form.get('Manufacturing science and engineering')
            str_mat_grade = request.form.get('Engineering mechanics/Strength of materials')
            app_thermo_grade = request.form.get('Applied thermodynamics')
            mt_grade = request.form.get('Mechatronics')
            fm_grade = request.form.get('Fluid mechanics')
            input_text = f"My CGPA is {cgpa}, I am from {branch} branch, I have scored {man_sci_eng_grade} in Manufacturing science and engineering,{str_mat_grade} in Engineering mechanics/Strength of materials,{app_thermo_grade} in Applied thermodynamics,{mt_grade} in Mechatronics and {fm_grade} in Fluid mechanics, I have done my specialisation in {specialisation}, I have done my minor in {minor}, I have done {internships} internships and {projects} projects should I persue Higher Education or Job?"

        elif branch == 'Civil':
            # Extract grades for Civil courses
            sa_grade = request.form.get('Structure analysis')
            str_ma_grade = request.form.get('Strength of materials')
            hyd_grade = request.form.get('Hydraulic engineering')
            soil_mnf_grade = request.form.get('Soil mechanics and foundation engineering')
            dss_grade = request.form.get('Design of steel structures')
            input_text = f"My CGPA is {cgpa}, I am from {branch} branch, I have scored {sa_grade} in MStructure analysis,{str_ma_grade} in Strength of materials,{hyd_grade} in Hydraulic engineering,{soil_mnf_grade} in Soil mechanics and foundation engineering and {dss_grade} in Design of steel structures, I have done my specialisation in {specialisation}, I have done my minor in {minor}, I have done {internships} internships and {projects} projects should I persue Higher Education or Job?"

                 
        
        #input_text = f"My CGPA is {cgpa}, I am from {branch} branch, I have done my specialisation in {specialisation}, I have done my minor in {minor}, I have done {internships} internships and {projects} projects should I persue Higher Education or Job?"

        response = model.generate_content(input_text)
        result = to_html(Markdown(response.text))
        return render_template('index.html', result=result, input_text=input_text)
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
