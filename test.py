import BuildSimHubAPI as bshapi
import time

bsh = bshapi.BuildSimHubAPIClient()

# 1. define the absolute directory of your energy model
file_dir = "/Users/weilixu/Desktop/5ZoneAirCooled.idf"
wea_dir="/Users/weilixu/Desktop/USA_CO_Golden-NREL.724666_TMY3.epw"
# 2. this is optional
new_sj = bsh.new_simulation_job()
# 3. start the API call
# note if fast simulation, call increaseAgents to increase the agent numbers
# response = newSj.create_run_model(file_dir)
response = new_sj.run(file_dir, wea_dir)
print(new_sj.trackToken)

if response == 'success':
    while new_sj.track_simulation():
        print (new_sj.trackStatus)
        time.sleep(5)

    response = new_sj.get_simulation_results('html')

    value_dict = bshapi.htmlParser.extract_value_from_table(response, 'Annual Building Utility Performance Summary',
      'Site and Source Energy', 'Energy Per Total Building Area', 'Net Site Energy')

    print(value_dict['value'] + " " + value_dict['unit'])

else:
    print(response)
