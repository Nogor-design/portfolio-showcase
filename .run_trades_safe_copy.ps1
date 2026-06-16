$env:BYPASS_DEMO_LOGIN='true'
$env:TRADES_BYPASS_DEMO_LOGIN='true'
$env:ENABLE_OWNER_ADMIN_TOOLS='false'
$env:TRADES_OWNER_ADMIN='false'
$env:ENABLE_LOCAL_CUSTOMER_FILES='false'
Set-Location 'D:\a1-program-manager\demo_runtimes\trades-resource-dashboard-safe'
python -m streamlit run app.py --server.headless true --server.port 8505 --browser.gatherUsageStats false
