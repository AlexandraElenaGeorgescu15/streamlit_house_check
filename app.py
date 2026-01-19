import streamlit as st
import json

# --- 1. CONFIGURARE PAGINĂ ---
st.set_page_config(
    page_title="Checklist Mutare: Basic vs. Pro",
    page_icon="🏡",
    layout="centered",
    initial_sidebar_state="expanded"
)

# --- 2. STRUCTURA DE DATE REORGANIZATĂ (Must Have vs Nice to Have) ---
checklist_data = {
    "🍳 Bucătărie: Gătit & Electrocasnice": {
        "Must Have": [
            "Oale și tigăi (Set de bază)", "Cuțite ascuțite (Chef + Pâine)", "Tocător (Lemn/Plastic)", 
            "Fierbător apă (Kettle)", "Tigăi (Wok/Clătite)", "Făcăleț", "Sită / Strecurătoare", 
            "Deschizător conserve", "Deschizător sticle/Tirbușon", "Răzătoare", "Polonic & Spatule",
            "Coș de gunoi (sub chiuvetă)", "Suport tacâmuri sertar", "Scurgător vase",
            "Pâlnie", "Piatră/Dispozitiv ascuțit cuțite"
        ],
        "Nice to Have": [
            "Aparat cafea (Espressor/Capsule)", "Air Fryer / Multicooker", "Blender / Robot bucătărie",
            "Prăjitor pâine", "Cântar bucătărie digital", 
            "Aparat vidat alimente (Mâncare 3x mai rezistentă)", 
            "SodaStream (Adio baxuri de apă)", "Organizator rotativ (Lazy Susan)",
            "Ascuțitor electric de cuțite", "Termometru carne"
        ]
    },
    "🍽️ Bucătărie: Consumabile & Organizare": {
        "Must Have": [
            "Lichid vase & Bureți", "Saci menajeri (35L & 120L)", "Folie alimentară & Aluminiu",
            "Hârtie de copt", "Prosoape de hârtie", "Recipiente condimente de bază",
            "Caserole (Tupperware)", "Pungi Ziploc (diverse mărimi)", "Site scurgere chiuvetă (Sink Strainers)",
            "Cleme sigilare pungi", "Scobitori & Elastice bani"
        ],
        "Nice to Have": [
            "Organizatoare frigider", "Etichete borcane (Label Maker)", "Suport tabletă (pentru rețete)",
            "Tocător dedicat doar pentru carne", "Covorașe sertare (antiderapante)",
            "Suport vin", "Pahare Vin/Cocktail (Set complet)"
        ]
    },
    "🛁 Baie & Igienă Personală": {
        "Must Have": [
            "Perie WC", "Pompă desfundat (Plunger)", "Perdea duș & Inele", "Covoraș duș (textil/cauciuc)",
            "Prosoape (Corp, Față, Mâini)", "Hârtie igienică", "Dozator săpun", "Coș gunoi mic (cu capac)",
            "Racletă duș (Squeegee - Critic pt sticlă!)", "Uscător de păr"
        ],
        "Nice to Have": [
            "Covoraș Diatomit (Piatră absorbantă)",
            "Capac WC cu închidere lentă (Soft close)", "Capac WC cu Bideu / Duș igienic",
            "Suport periuțe sterilizator UV", "Cântar corporal Smart", "Oglindă cosmetică cu mărire",
            "Termofor (Sticlă apă caldă)", "Placă păr/Ondulator"
        ]
    },
    "🛏️ Dormitor & Garderobă": {
        "Must Have": [
            "Saltea & Protecție saltea", "Perne dormit", "Pilotă (sezonieră)", "Lenjerii pat (2 seturi)",
            "Umerașe (multe!)", "Coș rufe (murdare)"
        ],
        "Nice to Have": [
            "Topper Saltea (Memory Foam)", "Perne cu memorie", "Cuvertură decorativă",
            "Umerașe catifea (antiderapante)", "Saci vidați (economie spațiu)", 
            "Organizatoare sertare lenjerie", "Lumini ambientale sub pat"
        ]
    },
    "🧺 Curățenie & Mentenanță Casă": {
        "Must Have": [
            "Aspirator", "Mop & Găleată", "Mătură & Făraș", "Lavete microfibră (set mare)",
            "Soluții bază (Universal, Geamuri, WC, Clor)", "Bureți magici", "Mănuși menaj",
            "Uscător rufe (Stander metalic)", "Masă de călcat & Fier", "Rolă scame"
        ],
        "Nice to Have": [
            "Robot Aspirator (Roomba/Roborock)", "Aspirator vertical (fără fir)", 
            "Uscător rufe automat (Mașină)", "Aparat curățat cu aburi", 
            "Stație de călcat", "Coș organizator produse curățenie (Caddy)"
        ]
    },
    "🛠️ Scule & Reparații (Toolbox)": {
        "Must Have": [
            "Trusă scule bază (Ciocan, Șurubelnițe, Patent)", "Ruletă măsurat", "Cutter",
            "Cheie aerisit calorifere (Critic Iarna!)", "Lanternă puternică", 
            "Bandă izolieră & Scotch lat", "Super Glue", "WD-40 (Clasic)", 
            "Scară pliantă", "Set dibluri & șuruburi mix"
        ],
        "Nice to Have": [
            "Bormașină / Șurubelniță electrică", "Nivelă Laser / Boloboc", 
            "Lanternă frontală (Headlamp - Mâini libere)",
            "WD-40 Siliconic (pt. chedere geamuri termopan)", "Pistol de lipit cu silicon",
            "Organizator șuruburi", "Detector tensiune"
        ]
    },
    "🖥️ Tech & Home Office": {
        "Must Have": [
            "Router Wi-Fi", "Prelungitoare (minim 3)", "Baterii (AA, AAA)",
            "Birou & Scaun ergonomic", "Încărcătoare telefon", "Monitor & Periferice"
        ],
        "Nice to Have": [
            "Sistem Mesh Wi-Fi (Pt pereți groși/etaj)", "UPS (Sursă neîntreruptibilă Router/PC)", 
            "Prelungitor cu protecție (Surge)", "Distrugător documente (Shredder)", 
            "Imprimantă Wireless", "Management cabluri (Velcro/Clipsuri)", "Prize Inteligente (Smart Plugs)"
        ]
    },
    "🧘 Sănătate, Siguranță & Confort (Wellness)": {
        "Must Have": [
            "Trusă prim ajutor (Plasturi, Betadină, Analgezice)", "Termometru corporal",
            "Detector fum / Gaz", "Stingător incendiu", "Chei de rezervă", "Plase țânțari"
        ],
        "Nice to Have": [
            "Purificator Aer (anti-praf oraș)", "Umidificator (Iarna) / Dezumidificator", 
            "Termostat inteligent", "Cameră supraveghere", "Senzor inundație", 
            "Lampă veghe cu senzor mișcare (hol/baie)"
        ]
    },
    "🏡 Hol, Decor & Ospitalitate": {
        "Must Have": [
            "Covoraș intrare", "Cuier haine", "Suport pantofi", "Perdele / Jaluzele",
            "Becuri de rezervă", "Oglindă mare"
        ],
        "Nice to Have": [
            "Încălțător (Shoe horn)", "Umbrelă de oaspeți",
            "Papuci de casă (pentru oaspeți)", "Cartonaș QR Code Wi-Fi", 
            "Plante naturale", "Lumânări parfumate", "Boxă inteligentă (Alexa/Google)"
        ]
    },
    "🐾 Animale de Companie (Optional)": {
        "Must Have": [
            "Boluri mâncare/apă", "Litieră/Pungi", "Mâncare", "Lesă"
        ],
        "Nice to Have": [
            "Fântână apă automată", "Camera supraveghere animale", "Aspirator dedicat păr animale"
        ]
    }
}

# --- 3. FUNCȚII AUXILIARE ---

def count_items(data):
    """Calculează numărul total de itemi din structura nested."""
    total = 0
    for cat in data.values():
        total += len(cat.get("Must Have", [])) + len(cat.get("Nice to Have", []))
    return total

total_items = count_items(checklist_data)

# --- 4. GESTIONAREA STĂRII (Session State) ---
if 'checklist_state' not in st.session_state:
    st.session_state.checklist_state = {}

def reset_checklist():
    st.session_state.checklist_state = {}

# --- 5. INTERFAȚA UTILIZATOR (UI) ---

st.title("🏡 Checklist Mutare: The Master List")
st.markdown("""
**Ghidul Suprem pentru Mutare.** Structurat pe priorități:
* 🚨 **Must Have:** Nu te poți muta fără ele (sau vei regreta imediat).
* ✨ **Nice to Have:** Upgrade-uri de viață, confort și organizare pro.
""")

# -- Sidebar (Meniu Lateral) --
with st.sidebar:
    st.header("⚙️ Opțiuni")
    
    # Statistici
    checked = sum(1 for v in st.session_state.checklist_state.values() if v)
    
    # Calcul procentaj
    if total_items > 0:
        prog_percent = int((checked / total_items) * 100)
    else:
        prog_percent = 0
        
    st.metric("Progres Total", f"{prog_percent}%", f"{checked} / {total_items} articole")
    st.progress(prog_percent)
    
    st.markdown("---")
    
    # Export/Import JSON
    st.subheader("💾 Salvare Date")
    json_data = json.dumps(st.session_state.checklist_state)
    st.download_button(
        label="📥 Descarcă Lista (JSON)",
        data=json_data,
        file_name="checklist_mutare_master.json",
        mime="application/json",
        help="Salvează progresul tău pe calculator."
    )
    
    uploaded = st.file_uploader("Încarcă Listă Salvată", type=['json'])
    if uploaded:
        try:
            st.session_state.checklist_state = json.load(uploaded)
            st.success("Listă încărcată cu succes!")
            st.rerun()
        except:
            st.error("Fișier invalid.")
            
    st.markdown("---")
    if st.button("🗑️ Resetează Tot (Reset)"):
        reset_checklist()
        st.rerun()

# -- Corpul Principal --

if checked == total_items and total_items > 0:
    st.balloons()
    st.success("🎉 Felicitări! Casa ta este complet echipată la nivel PRO!")

st.markdown("---")

# Iterăm prin categorii
for cat_name, subcats in checklist_data.items():
    
    # Calculăm progresul pe categorie (Must + Nice)
    items_in_cat = subcats.get("Must Have", []) + subcats.get("Nice to Have", [])
    if not items_in_cat:
        continue
        
    cat_checked = sum(1 for i in items_in_cat if st.session_state.checklist_state.get(f"{cat_name}_{i}", False))
    cat_total = len(items_in_cat)
    
    # Determinăm iconița de stare
    state_icon = "✅" if cat_checked == cat_total else "🟦"
    if cat_checked == 0: state_icon = "⬜"
    
    # Deschidem automat categoriile 'Must Have' care nu sunt terminate
    expanded_default = False
    must_have_items = subcats.get("Must Have", [])
    must_checked = sum(1 for i in must_have_items if st.session_state.checklist_state.get(f"{cat_name}_{i}", False))
    if must_have_items and must_checked < len(must_have_items):
        expanded_default = True

    # Titlu Expander
    with st.expander(f"{state_icon} {cat_name} ({cat_checked}/{cat_total})", expanded=expanded_default):
        
        # --- SECȚIUNEA MUST HAVE ---
        if subcats.get("Must Have"):
            st.markdown("##### 🚨 Must Have (Esențial)")
            cols_must = st.columns(2)
            for i, item in enumerate(subcats["Must Have"]):
                key = f"{cat_name}_{item}"
                col = cols_must[i % 2]
                
                # Checkbox logic
                is_checked = st.session_state.checklist_state.get(key, False)
                if col.checkbox(item, value=is_checked, key=key):
                    st.session_state.checklist_state[key] = True
                else:
                    st.session_state.checklist_state[key] = False
        
        # Separator vizual dacă există ambele categorii
        if subcats.get("Must Have") and subcats.get("Nice to Have"):
            st.markdown("---")
        
        # --- SECȚIUNEA NICE TO HAVE ---
        if subcats.get("Nice to Have"):
            st.markdown("##### ✨ Nice to Have (Confort & Upgrade)")
            cols_nice = st.columns(2)
            for i, item in enumerate(subcats["Nice to Have"]):
                key = f"{cat_name}_{item}"
                col = cols_nice[i % 2]
                
                # Checkbox logic
                is_checked = st.session_state.checklist_state.get(key, False)
                if col.checkbox(item, value=is_checked, key=key):
                    st.session_state.checklist_state[key] = True
                else:
                    st.session_state.checklist_state[key] = False

# Footer
st.markdown("---")
st.caption("Aplicație generată cu Streamlit • Checklist organizat pe priorități")
