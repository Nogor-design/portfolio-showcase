$env:ENABLE_OWNER_ADMIN_TOOLS='false'
$env:TRADES_OWNER_ADMIN='false'
$env:ENABLE_LOCAL_CUSTOMER_FILES='false'
$env:BYPASS_DEMO_LOGIN='true'
$env:TRADES_BYPASS_DEMO_LOGIN='true'
Set-Location 'D:\trades-resource-dashboard'
python -m streamlit run app.py --server.headless true --server.port 8504 --browser.gatherUsageStats false
