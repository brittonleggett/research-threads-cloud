import textstat

shared_flock = "The city of Meridian Falls recently installed automated license-plate-reader cameras at intersections around the city. The cameras photograph the license plates of passing vehicles and check them against law-enforcement databases. City officials said the cameras are meant to help local police solve crimes such as car theft."

flock = {
"Neutral": "The cameras began operating within a few weeks of installation, and the city posted basic information about the new system on its public works website. Local news covered the change as part of a routine story about city infrastructure.",
"Safety-benefit": "Two months after the cameras went live, they helped police identify a car connected to a string of home burglaries in the area. Police said the arrest would not have happened as quickly without the camera network.",
"Broad-network-access": "The camera network is connected to a national database that many other police departments use. Departments in other cities and states can search this database for camera information collected in Meridian Falls.",
"Disparate-impact": "An independent analysis of camera locations found that minority and lower-income neighborhoods had far more cameras installed than other parts of the city. Some neighborhoods had several cameras within a few blocks, while others had none.",
}

shared_ccs = "The Louisiana Department of Energy and Natural Resources is reviewing a permit application for a new well that would inject and store carbon dioxide deep underground in a rural parish. The well would operate under the state's federal-approved permitting program, with the EPA's Region 6 office providing oversight, and the company says the project will reduce emissions from nearby industrial facilities."

ccs = {
"No consultation": "State regulators reviewed the company's application and technical data on their own, following the same internal review process used for similar well permits. No public meetings or comment periods were held before the permit was approved.",
"Notice-only": "State regulators posted a public notice about the application on their website for two weeks before approving the permit. No public meetings were held, and none of the comments submitted during that time changed the final decision.",
"Affected-community": "Before deciding, state regulators held a public meeting in the parish where the well would be located and accepted written comments from residents. Several changes were made to the monitoring plan based on concerns raised at the meeting.",
"Broader-regional": "Before deciding, state regulators held public meetings in several parishes across the region and collected input from residents statewide. The permit conditions were revised based on that input before final approval.",
"Tribal-consultation": "Before deciding, state regulators formally consulted with the federally recognized tribal government whose historic lands include the project area, as required under tribal consultation procedures. The tribal government's input was incorporated into the final permit conditions.",
}

print("=== FLOCK (shared opening + condition) ===")
for name, cond in flock.items():
    full = shared_flock + " " + cond
    fk = textstat.flesch_kincaid_grade(full)
    fre = textstat.flesch_reading_ease(full)
    words = textstat.lexicon_count(full, removepunct=True)
    print(f"{name:20s}  FK grade={fk:5.1f}  Flesch Reading Ease={fre:6.1f}  words={words}")

print("\n=== CCS (shared opening + condition) ===")
for name, cond in ccs.items():
    full = shared_ccs + " " + cond
    fk = textstat.flesch_kincaid_grade(full)
    fre = textstat.flesch_reading_ease(full)
    words = textstat.lexicon_count(full, removepunct=True)
    print(f"{name:20s}  FK grade={fk:5.1f}  Flesch Reading Ease={fre:6.1f}  words={words}")
