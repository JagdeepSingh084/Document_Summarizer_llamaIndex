# Startup Project Assistant

This Smart job finder tool will help the user to find the perfect startup from a ppt which have various different startup projects to apply for depending upon the past experience and resume supplied in docs and pdf documents.

This POC demonstrate the llamaIndex implementation for summarizing and searching through various document formats present locally and are customizable according to user need with integration of chromadb vector database.

Important parameters:

## Configurations
CONFIG = {
    "DIRECTORY_PATH": "D:\\AppBulls\\LLM Application Frameworks\\llama_index\\llamaIndex_modules\\Directory_Summarizer\\documents",
    "file_extensions": ['.docx', '.pptx', '.txt', '.pdf'],
    "chunk_size": 512,
    "chunk_overlap": 64,
    "similarity_top_k": 5,
    "model_name": "gpt-4o",
    "temperature": 0.3
}


**query_mode**  = aquery() # Treat new query as fresh query with considering previous query results

**Agent** = functionAgent

### INPUT Documents:

Startup_projects.ppt
Past_experience.docs
Resume.pdf

#### User Input:
Job Projects Assistant (type 'exit' to quit)
Some example queries you can try:     
1. What startups match my skills and experience?
2. Find me jobs based on my resume    
3. Which startup would be the best fit for me?
4. bye

#### Output:
**You**: what startup projects present in the pptx file should I apply for what perfectly matches with my skills and experience provided in docs and pdf files formats

**Assistant**: Based on the information extracted from the documents, here are some startup projects from the "Deep Tech Startups Session IV" presentation that align well with your skills and experience as a Data Science Intern specializing in AI and backend development:

1. AI Enabled Technologies
   - AI-based Sorting Machine Your experience with AI and machine learning models like KNN, as well as your work with Langchain for creating AI agents, makes you a good fit for projects involving AI-based sorting and classification.

2. Medical Devices and Restorative Technologies
   - Computer Aided Diagnosis (CAD) Systems: Your background in AI and data science could be valuable in developing CAD systems for early-stage detection of diseases, leveraging your skills in data handling and machine learning.

3. Drone Based Research Facilities:
   - Real-time Data Logging and Live-Stream of Videos: Your experience with backend development and API integration could be beneficial in projects involving real-time data processing and streaming.

4. Forensic Research Facilities:
   - AI-enabled Low-cost Handheld Device for Writer Verification: Your skills in AI and machine learning could contribute to developing AI-enabled devices for forensic applicatd machine learning could contribute to developing AI-enabled devices for forensic applications.
ions.


5. Energy Scavenging & Management Tech:
   - Fabrication of Energy Harvester for Biomedical App5. Energy Scavenging & Management Tech:
   - Fabrication of Energy Harvester for Biomedical Applications: While this is more on the hardware side,   - Fabrication of Energy Harvester for Biomedical Applications: While this is more on the application*: While this is more old experience in integrating technologies could be useful in interdisciplinary project experience in integrating technologies could be useful in interdisciplinary projects.

These projects leverage your skills in AI, machine learning, backend development, and API integration, making them suitable opportunities for you to consider applying to.

Potentials:
Can be Used to Summarize and extract text from various different file formats and can be customized to chat based or query based Interactions with user.
