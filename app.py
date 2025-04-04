from flask import Flask, render_template, request

app = Flask(__name__)

# Breadcrumb mapping dictionary - maps URL paths to readable titles
BREADCRUMB_MAPPING = {
    '': 'Home',
    'courses': 'Courses',
    'math': 'Math',
    'reading-and-writing': 'Reading & Writing',
    'about': 'About',
    'contact': 'Contact',
    'qa': 'Q&A',
    'tips-and-hacks': 'Tips & Hacks',
    'resources': 'Resources',
    'what-to-expect-on-sat-math': 'What to Expect',
    'algebra': 'Algebra',
    'sat-prep-roadmap': 'Prep Roadmap',
    'solving-linear-equations-inequalities-beginner': 'Beginner: Linear Equations & Inequalities',
    'linear-equation-word-problems-beginner': 'Beginner: Linear Equations Word Problems',
    'linear-relationship-word-problems-beginner': 'Beginner: Linear Relationship Word Problems',
    'graphs-linear-equations-functions-beginner': 'Beginner: Graphs & Functions',
    'solving-linear-equations-inequalities-intermediate': 'Intermediate: Linear Equations & Inequalities',
    'linear-equation-word-problems-intermediate': 'Intermediate: Linear Equations Word Problems',
    'linear-relationship-word-problems-intermediate': 'Intermediate: Linear Relationship Word Problems',
    'graphs-linear-equations-functions-intermediate': 'Intermediate: Graphs & Functions',
    'solving-linear-equations-inequalities-advanced': 'Advanced: Linear Equations & Inequalities',
    'linear-equation-word-problems-advanced': 'Advanced: Linear Equations Word Problems',
    'linear-relationship-word-problems-advanced': 'Advanced: Linear Relationship Word Problems',
    'graphs-linear-equations-functions-advanced': 'Advanced: Graphs & Functions',
}

# Context processor to make the breadcrumb generator available to all templates
@app.context_processor
def utility_processor():
    def auto_breadcrumbs(path):
        # Special case for home page - don't show any breadcrumbs
        if path == '/' or path == '':
            return []
            
        # Remove leading and trailing slashes and split the path
        path = path.strip('/')
        parts = path.split('/')
        
        result = []
        
        # Define top-level sections that should directly connect to home
        top_level_sections = ['about', 'contact', 'qa', 'tips-and-hacks']
        
        # For top-level sections, only show Home > Section
        if len(parts) == 1 and parts[0] in top_level_sections:
            title = BREADCRUMB_MAPPING.get(parts[0], parts[0].replace('-', ' ').title())
            return [{
                'url': '/' + parts[0],
                'title': title
            }]
        
        # Special case for "courses" section
        if parts[0] == 'courses':
            return [{
                'url': '/courses',
                'title': 'Courses'
            }]
        
        # For math or reading-and-writing, always show under courses
        if parts[0] in ['math', 'reading-and-writing']:
            # Add courses as parent
            result.append({
                'url': '/courses',
                'title': 'Courses'
            })
            
            # Process the rest of the path
            current_path = ''
            for part in parts:
                if current_path:
                    current_path += '/' + part
                else:
                    current_path = part
                    
                # Use the mapping or capitalize the part if not in mapping
                title = BREADCRUMB_MAPPING.get(part, part.replace('-', ' ').title())
                
                # Add to result list
                result.append({
                    'url': '/' + current_path,
                    'title': title
                })
                
            return result
            
        # Default handling for other paths
        current_path = ''
        for part in parts:
            if current_path:
                current_path += '/' + part
            else:
                current_path = part
                
            # Use the mapping or capitalize the part if not in mapping
            title = BREADCRUMB_MAPPING.get(part, part.replace('-', ' ').title())
            
            # Add to result list
            result.append({
                'url': '/' + current_path,
                'title': title
            })
            
        return result
        
    return {'auto_breadcrumbs': auto_breadcrumbs}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/courses')
def courses():
    return render_template('courses.html')

@app.route('/math')
def math():
    return render_template('math.html')

@app.route('/math/sat-prep-roadmap')
def sat_prep_roadmap():
    return render_template('sat_prep_roadmap.html')

@app.route('/math/algebra')
def algebra_beginner():
    return render_template('algebra.html')

@app.route('/math/algebra/solving-linear-equations-inequalities-beginner')
def algebra_beginner_linear_equations():
    return render_template('algebra/solving_linear_equations_inequalities_beginner.html')

@app.route('/math/algebra/linear-equation-word-problems-beginner')
def algebra_beginner_word_problems():
    return render_template('algebra/linear_equation_word_problems_beginner.html')

@app.route('/math/algebra/linear-relationship-word-problems-beginner')
def algebra_beginner_relationship_problems():
    return render_template('algebra/linear_relationship_word_problems_beginner.html')

@app.route('/math/algebra/graphs-linear-equations-functions-beginner')
def algebra_beginner_graphs():
    return render_template('algebra/graphs_linear_equations_functions_beginner.html')

@app.route('/math/algebra/solving-linear-equations-inequalities-intermediate')
def algebra_intermediate_linear_equations():
    return render_template('algebra/solving_linear_equations_inequalities_intermediate.html')

@app.route('/math/algebra/linear-equation-word-problems-intermediate')
def algebra_intermediate_word_problems():
    return render_template('algebra/linear_equation_word_problems_intermediate.html')

@app.route('/math/algebra/linear-relationship-word-problems-intermediate')
def algebra_intermediate_relationship_problems():
    return render_template('algebra/linear_relationship_word_problems_intermediate.html')

@app.route('/math/algebra/graphs-linear-equations-functions-intermediate')
def algebra_intermediate_graphs():
    return render_template('algebra/graphs_linear_equations_functions_intermediate.html')

@app.route('/math/algebra/solving-linear-equations-inequalities-advanced')
def algebra_advanced_linear_equations():
    return render_template('algebra/solving_linear_equations_inequalities_advanced.html')

@app.route('/math/algebra/linear-equation-word-problems-advanced')
def algebra_advanced_word_problems():
    return render_template('algebra/linear_equation_word_problems_advanced.html')

@app.route('/math/algebra/linear-relationship-word-problems-advanced')
def algebra_advanced_relationship_problems():
    return render_template('algebra/linear_relationship_word_problems_advanced.html')

@app.route('/math/algebra/graphs-linear-equations-functions-advanced')
def algebra_advanced_graphs():
    return render_template('algebra/graphs_linear_equations_functions_advanced.html')

@app.route('/reading-and-writing')
def reading_writing():
    return render_template('reading_writing.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/what-to-expect-on-sat-math')
def what_to_expect_on_sat_math():
    return render_template('what_to_expect_on_sat_math.html')

@app.route('/qa')
def qa():
    return render_template('qa.html')

@app.route('/tips-and-hacks')
def tips_and_hacks():
    return render_template('tips_and_hacks.html')

@app.route('/resources')
def resources():
    return render_template('resources.html')

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', hide_breadcrumbs=True), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)