import streamlit as st
import json

# --- 1. CONFIGURARE PAGINĂ ---
st.set_page_config(
    page_title="Checklist Mutare Casă Nouă",
    page_icon="🏠",
    layout="centered",
    initial_sidebar_state="expanded"
)

# --- 2. DATELE (Checklist-ul Complet) ---
checklist_data = {
    "🍳 Bucătărie: Electrocasnice & Gătit": [
        "Aparat cafea / Presă franceză", "Fierbător apă", "Cuptor microunde", "Prăjitor pâine", 
        "Blender", "Cântar bucătărie", "Linguri măsurat", "Cană gradată", "Boluri mixare", 
        "Făcăleț", "Sită", "Tel", "Grătar răcire prăjituri", "Formă brioșe",
        "Vas Casserole/Termorezistent", "Oale și tigăi (Set)", "Wok", "Tăvi cuptor", "Formă Pizza",
        "Capac microunde", "Suport oale fierbinți"
    ],
    "🍴 Bucătărie: Ustensile & Organizare": [
        "Deschizător sticle", "Răzătoare brânză", "Feliator brânză", "Tocătoare (Lemn/Plastic)", 
        "Strecurătoare", "Tirbușon", "Pahare ouă", "Timer ouă", "Paletă pește", "Presă usturoi", 
        "Storcător citrice", "Feliator Pizza", "Zdrobitor cartofi", "Foarfecă bucătărie", 
        "Spatulă", "Deschizător conserve", "Clește bucătărie", "Curățător legume (Peeler)", 
        "Linguri de lemn", "Scurgător vase", "Suport tacâmuri sertar", "Folie alimentară", 
        "Tablete mașină spălat vase", "Suport prosoape hârtie", "Recipiente condimente", 
        "Caserole (Tupperware)", "Folie aluminiu", "Lichid vase", "Suport vin", "Coș fructe"
    ],
    "🍽️ Bucătărie: Servirea Mesei": [
        "Boluri supă/cereale", "Suporturi pahare", "Shaker cocktail", "Furculițe masă", 
        "Furculițe desert", "Pahare apă", "Lingură înghețată", "Cuțite masă", "Cuțite friptură", 
        "Set cuțite ascuțite", "Polonic", "Cană lapte", "Căni cafea/ceai", "Farfurii întinse", 
        "Farfurii desert", "Linguri supă", "Lingurițe ceai", "Ceainic", "Tavă servire", 
        "Carafă apă", "Frapieră", "Pahare vin"
    ],
    "🧤 Bucătărie: Textile": [
        "Șorț bucătărie", "Prosoape hârtie", "Șervețele masă", "Mănuși cuptor", "Prosoape bucătărie"
    ],
    "🛁 Baie: Esențiale": [
        "Perdea duș", "Covoraș duș (antiderapant)", "Etajeră duș", "Pompă desfundat (Plunger)", 
        "Perie WC", "Dozator săpun", "Suport prosoape", "Cântar corporal", "Prosoape baie (mari)", 
        "Prosoape față", "Prosoape mâini", "Șervețele cutie", "Hârtie igienică"
    ],
    "🛏️ Dormitor": [
        "Cuvertură pat", "Cearșafuri pat", "Husă pilotă", "Protecție saltea", "Fețe pernă", 
        "Protecții perne", "Pilotă (vară/iarnă)", "Perne dormit", "Suport pantofi", "Umerașe"
    ],
    "🧺 Spălătorie & Haine": [
        "Uscător rufe (stander)", "Bile uscător/Șervețele", "Fier de călcat", "Masă de călcat", 
        "Sac spălare delicate", "Coșuri rufe (Sortare)", "Detergent rufe", "Trusă cusut"
    ],
    "🧹 Curățenie": [
        "Clor/Înălbitor", "Soluție curățat baia", "Spray dezinfectant", "Soluție pete covoare", 
        "Soluție cuptor", "Soluție universală", "Soluție geamuri", "Saci menajeri", 
        "Coșuri gunoi", "Găleată și Mop", "Coș produse (Caddy)", 
        "Lavete microfibră", "Pămătuf praf", "Mănuși cauciuc", "Perii frecat", "Racletă geam", 
        "Făraș", "Mătură", "Aspirator"
    ],
    "🖼️ Decor & Atmosferă": [
        "Jaluzele/Rulouri", "Cordoane perdele", "Perdele/Draperii", "Perne decorative", "Pături (Throws)", 
        "Covor", "Veioze/Lămpi", "Becuri rezervă", "Rame foto", "Oglinzi", 
        "Ceas perete", "Lumânări", "Plante", "Vază flori"
    ],
    "🌳 Grădină & Exterior": [
        "Grătar (BBQ)", "Ustensile Grătar", "Mănuși grădinărit", "Scaunel grădinărit", "Furtun apă", 
        "Mașină tuns iarba", "Coș cârlige rufe", "Foarfecă pomi", "Greblă", "Foarfecă mare", 
        "Mistrie", "Stropitoare", "Mătură curte", "Lacăt magazie", "Frânghie rufe", "Cârlige rufe"
    ],
    "🛠️ Scule & Bricolaj": [
        "Pensule vopsit", "Folie protecție", "Trafalet", "Șpaclu", "Tavă vopsea", 
        "Cutter", "Bormașină", "Ciocan", "Ruletă măsurat", "Clește", 
        "Șurubelnițe (Set)", "Bandă adezivă", "Trusă scule generală", "Lanternă", 
        "Protecții pâslă mobilă", "Rafturi/Polițe", "Scară pliantă", "Cutii depozitare", "Cârlige perete"
    ],
    "🔥 Siguranță": [
        "Detector monoxid carbon", "Detector fum", "Pătură ignifugă", "Stingător incendiu", 
        "Trusă prim ajutor", "Sistem alarmă", "Cameră securitate"
    ],
    "💡 Diverse & Extra": [
        "Baterii (AA, AAA)", "Cuier haine", "Opritor ușă", "Prelungitoare", "Suport chei", 
        "Chibrituri/Brichetă", "Bandă scotch", "Suport umbrele", "WD-40", "Covoraș intrare",
        "Router Wi-Fi & Cabluri", "Dosar acte casă", "Chei de rezervă", "Trusă medicamente"
    ],
    "🧐 Must-haves (Uitate des, dar critice)": [
        "Site scurgere chiuvetă (Sink Strainers)", "Plase de țânțari", "Filtru apă / Cană filtrantă",
        "Organizatoare cabluri (Velcro/Zip ties)", "Pâslă picioare mobilă (extra stoc)",
        "Set chei de rezervă (la prieteni)", "Organizator sertar 'Junk Drawer'", "Capace WC noi"
    ],
    "💎 Extra Fancy (Upgrade-uri de viață)": [
        "Robot Aspirator", "Uscător Rufe (Mașină separată)", "Termostat Inteligent",
        "Air Fryer / Multicooker", "Lumini Inteligente / Dimmere",
        "Capac WC cu Bideu / Duș igienic", "Topper Saltea Memory Foam"
    ]
}

# Calculăm totalul elementelor
total_items = sum(len(items) for items in checklist_data.values())

# --- 3. GESTIONAREA STĂRII (Session State) ---
# Inițializăm starea dacă nu există
if 'checklist_state' not in st.session_state:
    st.session_state.checklist_state = {}

# Funcție pentru resetare
def reset_checklist():
    st.session_state.checklist_state = {}

# --- 4. INTERFAȚA UTILIZATOR (UI) ---

st.title("🏠 Checklist Mutare Casă Nouă")
st.markdown(f"**201+ Articole Esențiale** pentru o mutare fără stres.")

# -- Bara laterală (Sidebar) pentru Control --
with st.sidebar:
    st.header("⚙️ Opțiuni")
    
    # Salvare/Încărcare Progres
    st.subheader("Salvare Progres")
    # Buton Download
    json_string = json.dumps(st.session_state.checklist_state)
    st.download_button(
        label="📥 Descarcă Checklist (JSON)",
        file_name="progres_mutare.json",
        mime="application/json",
        data=json_string,
        help="Descarcă progresul actual pentru a-l încărca mai târziu."
    )
    
    # Buton Upload
    uploaded_file = st.file_uploader("Încarcă Progresul Salvat", type=['json'])
    if uploaded_file is not None:
        try:
            data = json.load(uploaded_file)
            st.session_state.checklist_state = data
            st.success("Progres încărcat cu succes!")
            st.rerun()
        except:
            st.error("Fișier invalid.")

    st.markdown("---")
    if st.button("⚠️ Resetează Tot Checklist-ul"):
        reset_checklist()
        st.rerun()

# -- Bara de Progres Principală --
checked_count = sum(1 for v in st.session_state.checklist_state.values() if v)
progress_percent = int((checked_count / total_items) * 100)

col1, col2 = st.columns([3, 1])
with col1:
    st.progress(progress_percent)
with col2:
    st.metric("Progres", f"{progress_percent}%", f"{checked_count}/{total_items} articole")

if progress_percent == 100:
    st.balloons()
    st.success("Felicitări! Ai tot ce îți trebuie pentru casa nouă! 🎉")

st.markdown("---")

# -- Afișarea Categoriilor --
# Iterăm prin dicționar
for category, items in checklist_data.items():
    # Calculăm câte sunt bifate în această categorie pentru a afișa în titlu
    cat_checked = sum(1 for item in items if st.session_state.checklist_state.get(f"{category}_{item}", False))
    cat_total = len(items)
    
    # Titlu expander dinamic
    expander_title = f"{category} ({cat_checked}/{cat_total})"
    
    # Pentru noile categorii, le punem să fie deschise automat dacă nu sunt completate
    default_expanded = (cat_checked > 0 and cat_checked < cat_total)
    if "Must-haves" in category or "Extra Fancy" in category:
        default_expanded = True
    
    with st.expander(expander_title, expanded=default_expanded):
        # Facem un grid de 2 coloane pentru aspect mai compact
        cols = st.columns(2)
        for i, item in enumerate(items):
            # Cheie unică pentru fiecare checkbox
            key = f"{category}_{item}"
            
            # Determinăm coloana (stânga sau dreapta)
            col = cols[i % 2]
            
            # Checkbox-ul propriu-zis
            is_checked = st.session_state.checklist_state.get(key, False)
            checked = col.checkbox(item, value=is_checked, key=key)
            
            # Actualizăm starea
            st.session_state.checklist_state[key] = checked

# Footer
st.markdown("---")
st.caption("Creat cu ❤️ folosind Streamlit. Sursă date: Knight Frank New House Checklist + Extra Tips.")
