URL="https://services.empirix.com/"
Loginid="QA_traininguser23"
Password="Empirix!"

#modules_xpath
userid="//div/input[@type='text']"   
pasid="//div/input[@type='password']"
btnid="//div/input[@type='submit']"
rememid="//*[@id='remember']"
dropdown="//*[@class='dropdown-toggle ng-binding']"
Alert="//a[@data-i18n='_alerts_']"
Dashboard="(//a[@href='/dashboard'])[2]"
Tests="//a[@href='/tests']"
Variables="//a[@data-i18n='_variables_']"
Notificaton="//a[@data-i18n='_notifications_']"

#client_details_xpath
client="//span[contains(.,'Client')]"
c_details="//h3[text()='Client Details']"
c_name="//label[text()='Client Name']/following-sibling::label"
c_des="//label[text()='Description']/following-sibling::label"
s_date="//label[text()='Subscription Start Date']/following-sibling::label"
e_date="//label[text()='Subscription End Date']/following-sibling::label"
MLT="//label[text()='Maximum Load Tests']/following-sibling::label"
MVT="//label[text()='Maximum VoiceWatch Tests']/following-sibling::label"
scenerios="//label[text()='Maximum Scenarios']/following-sibling::label"
MTS="//label[text()='Minimum Test Schedule Period (mins)']/following-sibling::label"