from flask import render_template, jsonify

def configure_routes(app, api_service):

    @app.route('/')
    def index():
        try:
            data = api_service.get_vaccination_data()
            return render_template('index.html', data=data)
        except requests.HTTPError as e:
            return jsonify({'error': str(e)}), e.response.status_code

    @app.route('/vaccinations/<int:year>')
    def vaccinations_by_year(year):
        try:
            data = api_service.get_vaccination_by_year(year)
            return render_template('details.html', year=year, data=data)
        except requests.HTTPError as e:
            return jsonify({'error': str(e)}), e.response.status_code
