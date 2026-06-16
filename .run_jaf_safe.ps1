$env:JAF_DATA_DIR='D:\a1-program-manager\demo_runtimes\jaf-data'
Set-Location 'D:\JobApplicationFactory'
python -m streamlit run app/main.py --server.headless true --server.port 8506 --browser.gatherUsageStats false
