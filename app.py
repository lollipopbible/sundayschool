from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kids Bible Church</title>
    <style>
        body {
            font-family: 'Comic Sans MS', cursive, sans-serif;
            background-color: #fff5e6;
            margin: 0;
            padding: 0;
        }
        .top-bar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: linear-gradient(90deg, #8b4513, #708090, #4682b4, #2f4f4f);
            padding: 10px 20px;
            border-bottom: 5px solid #5f9ea0;
            color: white;
            animation: fadeColors 120s infinite;
        }
        @keyframes fadeColors {
            0% { background: linear-gradient(90deg, #8b4513, #708090, #4682b4, #2f4f4f); color: #ffffff; }
            25% { background: linear-gradient(90deg, #5f9ea0, #8b4513, #2f4f4f, #708090); color: #ffffff; }
            50% { background: linear-gradient(90deg, #2f4f4f, #4682b4, #5f9ea0, #8b4513); color: #ffffff; }
            75% { background: linear-gradient(90deg, #708090, #5f9ea0, #8b4513, #4682b4); color: #ffffff; }
            100% { background: linear-gradient(90deg, #8b4513, #708090, #4682b4, #2f4f4f); color: #ffffff; }
        }
        .top-bar h4 {
            margin: 0;
            font-size: 1.5rem;
        }
        .user-circle {
            background-color: #fff;
            color: #8b4513;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 1rem;
            font-weight: bold;
            border: 2px solid #8b4513;
        }
        .left-section {
            background-color: #f5f5dc;
            padding: 20px;
            width: 200px;
            height: calc(100vh - 60px);
            float: left;
        }
       .left-section.hidden {
            width: 0px;
            padding: 0px;
            overflow: hidden;
        }
        .left-section h4 {
            color: #8b4513;
            margin-top: 0;
        }
        .left-section a {
            display: flex;
            align-items: center;
            text-decoration: none;
            color: #8b4513;
            font-size: 1rem;
            margin: 5px 0;
        }
        .left-section a:hover {
            color: #5f9ea0;
        }
        .left-section a::before {
            content: '\\1F36D'; /* Unicode for lollipop emoji */
            margin-right: 10px;
        }
        .main-section {
            margin-left: 220px;
            padding: 20px;
            background-color: #fff;
            min-height: calc(100vh - 120px);
            text-align: center;
        }
        .bottom-bar {
            position: fixed;
            bottom: 0;
            width: 100%;
            background-color: #5f9ea0;
            padding: 10px;
            display: flex;
            align-items: center;
        }
        .bottom-bar input {
            flex: 1;
            padding: 10px;
            border: 2px solid #8b4513;
            border-radius: 5px;
            margin-right: 10px;
        }
        .bottom-bar button {
            background-color: #8b4513;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            font-size: 1rem;
            cursor: pointer;
        }
        .bottom-bar button:hover {
            background-color: #2f4f4f;
        }
        iframe {
            width: 95%;
            height: 80vh;
            border: none;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="top-bar" onclick="toggleSidebar()">
        <h4>Kids Bible Church</h4>
        <div class="user-circle">KM</div>
    </div>
    <div class="container">
        <div class="left-section" id="sidebar">
            <h4>Lesson</h4>
            <a href="#" onclick="showVideo('https://www.youtube.com/embed/YhAH2zU8UiU')">I Wont Be Afraid</a><br>
           <a href="#" onclick="showVideo('https://www.youtube.com/embed/6FOLl7AGRoI')">Big and Strong</a><br>
              <a href="#" onclick="showPDF('/pdf/EC_Gladiator_Week_1.01.pdf')">Lesson</a><br>
            <h4>Roles</h4>
            <h4>Activities</h4>
        </div>
        <div class="main-section" id="main-section">
            <iframe src="https://www.youtube.com/embed/6FOLl7AGRoI" allowfullscreen></iframe>
        </div>
    </div>
    <div class="bottom-bar">
        <input type="text" id="command-input" placeholder="Type your command here...">
        <button onclick="alert('Command sent!')">Send</button>
    </div>
    <br><br><br><br><br><br><br>
    <script>
        function showVideo(url) {
            document.getElementById('main-section').innerHTML = `
                <iframe src="${url}" allowfullscreen></iframe>
            `;
        }

        function showPDF(pdfUrl) {
            document.getElementById('main-section').innerHTML = `
                <iframe src="${pdfUrl}" type="application/pdf"></iframe>
            `;
        }

        function toggleSidebar() {
            const sidebar = document.getElementById('sidebar');
            sidebar.classList.toggle('hidden');
        }
        function showDropBoxPDF() {
            window.open("https://www.dropbox.com/scl/fi/1mhysp6mvbfj6dmrd72lk/EC_Gladiator_Week_1.01.pdf?rlkey=tkoi5z4tghiywcur1zedhllav&st=8fwxplee&dl=0", "_blank");
        }
    </script>
</body>
</html>
    """

@app.route('/pdf/<path:filename>')
def serve_pdf(filename):
    return send_from_directory('.', filename)

if __name__ == "__main__":
    app.run(debug=True)
