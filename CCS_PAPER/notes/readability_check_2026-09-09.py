import textstat

shared_ccs_v2 = "The Louisiana Department of Energy and Natural Resources is reviewing a request for a new well in a rural parish. The well would pump carbon dioxide gas deep underground for storage. The EPA's Region 6 office would also oversee the well. The company says the project will help cut pollution from nearby factories."

ccs_v2 = {
"No consultation": "State regulators looked at the company's request and technical data on their own. They followed the same process used for similar well permits. No public meetings were held before they approved it.",
"Notice-only": "State regulators posted a notice about the request on their website for two weeks. They did not hold any public meetings. None of the comments people sent in changed the final decision.",
"Affected-community": "Before deciding, state regulators held a public meeting in the parish. They also accepted written comments from residents. They changed the monitoring plan based on concerns raised at the meeting.",
"Broader-regional": "Before deciding, state regulators held public meetings in several parishes. They also collected input from residents across the state. They changed the permit conditions based on that input.",
"Tribal-consultation": "Before deciding, state regulators consulted with the federally recognized tribal government whose historic lands include the project area. State rules require this consultation. The tribal government's input was included in the final permit conditions.",
}

print("=== CCS v2 (revised for readability) ===")
for name, cond in ccs_v2.items():
    full = shared_ccs_v2 + " " + cond
    fk = textstat.flesch_kincaid_grade(full)
    fre = textstat.flesch_reading_ease(full)
    words = textstat.lexicon_count(full, removepunct=True)
    sentences = textstat.sentence_count(full)
    print(f"{name:20s}  FK grade={fk:5.1f}  Reading Ease={fre:6.1f}  words={words}  sentences={sentences}")

# Flock revision pass
shared_flock_v2 = "The city of Meridian Falls set up license-plate cameras at intersections around the city. The cameras take photos of car plates and check them against police lists. City officials said the cameras will help police solve crimes such as car theft."

flock_v2 = {
"Neutral": "The cameras started working a few weeks after they went up. The city posted basic facts about the new cameras on its website. Local news covered the story as routine city news.",
"Safety-benefit": "Two months after the cameras went live, they helped police find a car linked to a string of home burglaries. Police said the arrest would not have happened as fast without the cameras.",
"Broad-network-access": "The camera network links to a national database that many other police departments use. Departments in other cities and states can search this database for camera data from Meridian Falls.",
"Disparate-impact": "A new study of camera locations found that minority and lower-income neighborhoods had far more cameras than other parts of the city. Some neighborhoods had several cameras nearby, while others had none.",
}

print("\n=== FLOCK v2 (revised for readability) ===")
for name, cond in flock_v2.items():
    full = shared_flock_v2 + " " + cond
    fk = textstat.flesch_kincaid_grade(full)
    fre = textstat.flesch_reading_ease(full)
    words = textstat.lexicon_count(full, removepunct=True)
    sentences = textstat.sentence_count(full)
    print(f"{name:20s}  FK grade={fk:5.1f}  Reading Ease={fre:6.1f}  words={words}  sentences={sentences}")
