# 🌐 ChatBot with Web Scrapy and Pre-trained LLMs  

## 🚀 Overview  
This project is a **ChatBot** designed to extract relevant information from websites using **Web Scrapy** and answer user queries intelligently. The bot leverages pre-trained Large Language Models (LLMs) from **Ollama** to process, analyze, and deliver contextually accurate responses to user queries.  

By combining web scraping with the power of advanced language models, the chatbot enables efficient and seamless information retrieval, especially for domain-specific tasks such as **health** and **education**.  

---

## ✨ Features  
- 🔎 **Web Scraping:** Efficiently extracts data from websites using **Web Scrapy**.  
- 🤖 **Intelligent Query Handling:** Processes user questions and provides meaningful answers.  
- 📚 **Pre-trained LLM Integration:** Utilizes **Ollama LLMs** to enhance the understanding of queries and data.  
- 🌐 **Domain-Specific Responses:** Specially tuned to provide information related to health and education topics.  
- ⚡ **Real-Time Interaction:** Engages users in real time, offering prompt and accurate responses.  

---

## 🛠️ Tech Stack  
- **Python**: Primary programming language.  
- **Web Scrapy**: For extracting data from websites.  
- **Ollama LLMs**: Pre-trained language models for query processing and response generation. 


---

## ⚙️ Setup and Installation  

1. **Install Dependencies**  
   Ensure you have Python installed. Then run:  
   ```bash
   pip install -r requirements.txt
   ```  

2. **Configure Web Scrapy**  
   Update the **web_scraper.py** file with the target website URLs and scraping logic.  

3. **Integrate Ollama LLMs**  
   Ensure you have access to **Ollama LLMs** and configure the API keys in the `query_processor.py` file.  

4. **Run the ChatBot**  
   ```bash
   python app.py
   ```  

5. **Interact with the Bot**  
   Open your browser and go to `http://localhost:5000` (if Flask/Django is used) or interact via the terminal.  

---

## 🚨 Limitations  
- Website scraping is subject to **robots.txt** restrictions and ethical considerations.  
- Responses are limited by the scope of the scraped data and the capabilities of the pre-trained LLM.  
- Internet access is required for web scraping and LLM API integration.  

---

## 🤝 Contributing  
Contributions are welcome! Please follow these steps:  
1. Fork the repository.  
2. Create a new branch (`feature/new-feature`).  
3. Commit your changes (`git commit -m 'Add a new feature'`).  
4. Push to the branch (`git push origin feature/new-feature`).  
5. Submit a pull request.  

---

## 📝 License  
This project is licensed under the [MIT License](LICENSE).  

---

## 📧 Contact  
If you have any questions or feedback, feel free to reach out:  
- **Author:** B. Chandravadhan Raj  
- **GitHub:** https://github.com/BCVRaj 


