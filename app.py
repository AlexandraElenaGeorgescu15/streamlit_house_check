import streamlit as st
import json
import pandas as pd

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Ultimate Move Checklist (251+ Items)",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. THE MASTER DATA (Original 201 + Modern Extras) ---
checklist_data = {
    "🍳 Bucătărie: Electrocasnice (Appliances)": {
        "Must Have": [
            "1. Aparat cafea / Presă franceză", "2. Fierbător apă (Kettle)", "3. Cuptor microunde", 
            "4. Prăjitor pâine", "32. Oale și tigăi (Set)", "35. Bol salată", 
            "36. Foarfecă bucătărie", "39. Deschizător conserve", "43. Wok", "16. Vas Casserole"
        ],
        "Nice to Have": [
            "5. Blender", "6. Formă brioșe (Cupcake tray)", "7. Cântar bucătărie", 
            "26. Storcător fructe (Juice extractor)", 
            "Air Fryer (Extra)", "SodaStream (Extra)", "Aparat vidat alimente (Extra)", "Sandwich Maker (Extra)"
        ]
    },
    "🔪 Bucătărie: Ustensile & Gătit": {
        "Must Have": [
            "8. Linguri măsurat", "9. Cană gradată", "10. Boluri mixare", "11. Făcăleț", 
            "12. Sită (Sieve)", "13. Tel (Whisk)", "15. Deschizător sticle", "17. Răzătoare", 
            "19. Tocătoare (Chopping boards)", "20. Strecurătoare (Colander)", "21. Tirbușon", 
            "24. Paletă pește (Fish slice)", "25. Presă usturoi", "31. Deschizător conserve (Tin opener)", 
            "34. Zdrobitor cartofi", "37. Spatulă", "40. Clește (Tongs)", "41. Curățător legume (Peeler)", 
            "44. Linguri de lemn"
        ],
        "Nice to Have": [
            "14. Grătar răcire prăjituri", "18. Feliator brânză", "22. Pahare ouă", 
            "23. Timer ouă", "27. Capac microunde", "28. Tăvi cuptor", "30. Feliator pizza",
            "31. Tavă pizza", "33. Suport oale fierbinți", "50. Lingură înghețată", 
            "52. Polonic", "Ascuțitor electric cuțite (Life Hack)", "Organizator capace oale (Extra)"
        ]
    },
    "🍽️ Bucătărie: Servire & Organizare": {
        "Must Have": [
            "45. Boluri", "48. Furculițe (Masă & Desert)", "49. Pahare", 
            "51. Cuțite (Unt, Steak, Chefi)", "54. Căni (Mugs)", "55. Farfurii (Întinse & Desert)", 
            "56. Linguri (Supă, Desert, Ceai)", "63. Cutie pâine", "64. Suport tacâmuri sertar", 
            "66. Tablete mașină spălat vase", "67. Scurgător vase", "70. Suport prosoape hârtie", 
            "71. Solnițe sare/piper", "73. Sită scurgere chiuvetă", "79. Lichid vase"
        ],
        "Nice to Have": [
            "38. Zaharniță", "42. Sticlă apă", "46. Suporturi pahare (Coasters)", 
            "47. Shaker cocktail", "53. Cană lapte", "57. Ceainic", "58. Tavă servire", 
            "59. Carafă apă", "60. Frapieră", "61. Pahare vin", "68. Coș fructe", 
            "69. Tavă cuburi gheață", "74. Raft condimente", "75. Organizator chiuvetă", 
            "80. Suport vin", "Organizator rotativ (Lazy Susan)", "Lumini LED sub dulapuri (Extra)"
        ]
    },
    "🧤 Bucătărie: Textile & Consumabile": {
        "Must Have": [
            "65. Folie alimentară", "72. Pungi sandwich", "77. Folie aluminiu", 
            "78. Caserole (Tupperware)", "82. Prosoape hârtie", "84. Mănuși cuptor", 
            "85. Prosoape bucătărie (Textil)"
        ],
        "Nice to Have": [
            "76. Cutie ceai", "81. Șorț", "83. Șervețele masă", "Etichetator/Label Maker (Extra)"
        ]
    },
    "🛁 Baie: Esențiale": {
        "Must Have": [
            "86. Perdea duș", "87. Covoraș duș", "89. Pompă desfundat (Plunger)", 
            "90. Perie WC", "91. Dozator săpun", "92. Suport prosoape", 
            "94. Prosoape baie (mari)", "96. Prosoape mâini", "98. Hârtie igienică",
            "Racletă duș/Squeegee (Original 162 - moved here)"
        ],
        "Nice to Have": [
            "62. Lighean (Basin)", "88. Etajeră duș", "93. Cântar corporal", 
            "95. Prosoape față", "97. Șervețele cutie", 
            "Covoraș Diatomit (Extra)", "Capac WC cu Bideu (Extra)"
        ]
    },
    "🛏️ Dormitor & Textile": {
        "Must Have": [
            "100. Cearșafuri pat", "101. Husă pilotă", "102. Protecție saltea", 
            "103. Fețe pernă", "105. Pilotă", "106. Perne", "107. Suport pantofi"
        ],
        "Nice to Have": [
            "99. Cuvertură pat", "104. Protecții perne", 
            "Topper Saltea Memory Foam (Extra)", "Lumini senzor dulap haine (Extra)", "Draperii Blackout (Extra)"
        ]
    },
    "🧺 Spălătorie & Îngrijire Haine": {
        "Must Have": [
            "108. Uscător rufe (Stander)", "110. Fier de călcat", "111. Masă de călcat", 
            "113. Coșuri rufe", "114. Detergent rufe", "115. Umerașe"
        ],
        "Nice to Have": [
            "109. Bile uscător / Șervețele", "112. Sac spălare delicate", "116. Trusă cusut", 
            "Steamer Vertical (Extra)", "Aparat curățat scame (Extra)", "Umerașe catifea (Extra)"
        ]
    },
    "🖼️ Decor & Atmosferă": {
        "Must Have": [
            "117. Jaluzele/Rulouri", "119. Perdele", "123. Veioze/Lămpi", 
            "124. Becuri rezervă", "126. Oglinzi"
        ],
        "Nice to Have": [
            "118. Cordoane perdele", "120. Perne decorative", "121. Pături (Throws)", 
            "122. Covor", "125. Rame foto", "127. Ceas perete", "128. Lumânări", 
            "129. Plante", "130. Vază", "Lampă veghe cu senzor (Extra)"
        ]
    },
    "🧹 Curățenie (Cleaning)": {
        "Must Have": [
            "147. Clor/Înălbitor", "148. Soluție baie", "149. Dezinfectant", 
            "152. Soluție universală", "153. Soluție geamuri", "154. Saci menajeri", 
            "155. Coșuri gunoi", "156. Găleată și Mop", "158. Lavete/Cârpe", 
            "160. Mănuși cauciuc", "163. Făraș", "164. Mătură", "165. Aspirator"
        ],
        "Nice to Have": [
            "150. Soluție pete covoare", "151. Soluție cuptor", "157. Coș produse (Caddy)", 
            "159. Pămătuf praf", "161. Perii frecat", 
            "Robot Aspirator (Extra)", "Mop cu pulverizator (Extra)", "Perie electrică rotativă (Extra)"
        ]
    },
    "🌳 Grădină & Exterior": {
        "Must Have": [
            "135. Furtun apă", "136. Mașină tuns iarba", "143. Mătură curte", 
            "145. Frânghie rufe", "146. Cârlige rufe"
        ],
        "Nice to Have": [
            "131. Grătar (BBQ)", "132. Ustensile BBQ", "133. Mănuși grădinărit", 
            "134. Scaunel grădinărit", "137. Coș cârlige", "138. Foarfecă pomi", 
            "139. Greblă", "140. Foarfecă mare", "141. Mistrie", "142. Stropitoare", 
            "144. Lacăt magazie"
        ]
    },
    "🛠️ Bricolaj (DIY Tools)": {
        "Must Have": [
            "171. Cutter", "172. Bormașină", "173. Ciocan", "174. Ruletă măsurat", 
            "175. Clește", "176. Șurubelnițe", "177. Bandă adezivă", "178. Trusă scule", 
            "179. Lanternă", "182. Scară pliantă"
        ],
        "Nice to Have": [
            "166. Pensule vopsit", "167. Folie protecție", "168. Trafalet", 
            "169. Șpaclu", "170. Tavă vopsea", "180. Protecții pâslă mobilă", 
            "181. Rafturi/Polițe", "183. Cutii depozitare", "184. Cârlige perete",
            "Cheie aerisit calorifere (Critical Extra)", "WD-40 Siliconic (Extra)"
        ]
    },
    "🔥 Siguranță & Sănătate": {
        "Must Have": [
            "185. Detector monoxid carbon", "186. Detector fum", "189. Trusă prim ajutor", 
            "192. Baterii", "195. Prelungitor", "200. WD40 (Clasic)", "201. Covoraș intrare",
            "Termometru corporal (Extra)", "Medicamente bază (Extra)"
        ],
        "Nice to Have": [
            "187. Pătură ignifugă", "188. Stingător incendiu", "190. Alarmă securitate", 
            "191. Cameră securitate", "193. Cuier haine", "194. Opritor ușă", 
            "196. Suport chei", "197. Chibrituri/Brichetă", "198. Scotch (Sellotape)", 
            "199. Suport umbrele", 
            "Dezumidificator (Life Hack)", "Purificator Aer (Life Hack)", "Higrometru (Life Hack)"
        ]
    },
    "🖥️ Home Office & Tech (Nou)": {
        "Must Have": [
            "Birou lucru", "Scaun ergonomic", "Monitor extern", "Prelungitor cu protecție", 
            "Laptop/PC", "Cabluri încărcare"
        ],
        "Nice to Have": [
            "Lampă birou", "Suport Laptop/Monitor", "Tastatură & Mouse", "Webcam", 
            "Imprimantă/Scanner", "Distrugător documente", "Priză turn/Cub USB-C", "Sistem Mesh Wi-Fi"
        ]
    },
    "🐾 Animale de Companie (Nou)": {
        "Must Have": [
            "Boluri mâncare/apă", "Mâncare", "Lesă/Zgardă", "Pungi igienice/Litieră"
        ],
        "Nice to Have": [
            "Pat/Culcuș", "Jucării", "Șampon animale", "Perie blană", "Transportor"
        ]
    }
}

# --- 3. HELPER FUNCTIONS ---
def get_total_items(data):
    count = 0
    for cat in data.values():
        count += len(cat.get("Must Have", [])) + len(cat.get("Nice to Have", []))
    return count

total_items_count = get_total_items(checklist_data)

# --- 4. SESSION STATE MANAGEMENT ---
# Initialize ONLY if not present to avoid overwriting on rerun
if 'checklist_state' not in st.session_state:
    st.session_state.checklist_state = {}

def toggle_item(item_key):
    """Callback to toggle item state"""
    if item_key in st.session_state.checklist_state:
        st.session_state.checklist_state[item_key] = not st.session_state.checklist_state[item_key]
    else:
        st.session_state.checklist_state[item_key] = True

def reset_all():
    st.session_state.checklist_state = {}
    st.rerun()

# --- 5. SIDEBAR (CONTROLS) ---
with st.sidebar:
    st.title("🎛️ Control Panel")
    
    # Progress
    checked_items = sum(1 for k, v in st.session_state.checklist_state.items() if v)
    progress_percentage = checked_items / total_items_count if total_items_count > 0 else 0
    
    st.metric("Total Progres", f"{int(progress_percentage * 100)}%", f"{checked_items}/{total_items_count} Articole")
    st.progress(progress_percentage)
    
    st.markdown("---")
    
    # Filters
    st.subheader("👀 Filtre Vizualizare")
    view_mode = st.radio("Arată:", ["Tot", "Doar Ne-bifate", "Doar 'Must Have'"])
    
    st.markdown("---")
    
    # Save/Load
    st.subheader("💾 Date")
    # Download
    json_str = json.dumps(st.session_state.checklist_state)
    st.download_button("📥 Descarcă Progres", json_str, "move_checklist_v4.json", "application/json")
    
    # Upload
    uploaded_file = st.file_uploader("Încarcă Progres", type=['json'])
    if uploaded_file:
        try:
            data = json.load(uploaded_file)
            st.session_state.checklist_state = data
            st.success("Date încărcate!")
            time.sleep(1) # Give user time to see success
            st.rerun()
        except Exception as e:
            st.error(f"Eroare: {e}")
            
    if st.button("🗑️ Resetare Completă", type="primary"):
        reset_all()

# --- 6. MAIN CONTENT ---
st.title("🏠 Ultimate Move Checklist")
st.markdown(f"**251+ Articole** | Organizate | Prioritizate | Smart")

# Tabs for UX
tab_list, tab_shop, tab_stats = st.tabs(["📝 Checklist", "🛒 Listă Cumpărături", "📊 Statistici"])

# --- TAB 1: CHECKLIST ---
with tab_list:
    # Search Bar
    search_term = st.text_input("🔍 Caută un obiect...", "").lower()

    for category, subcats in checklist_data.items():
        # Flatten for search check
        all_cat_items = subcats.get("Must Have", []) + subcats.get("Nice to Have", [])
        
        # 1. Filter by Search
        if search_term:
            matched_items = [i for i in all_cat_items if search_term in i.lower()]
            if not matched_items:
                continue # Skip category if search doesn't match
        else:
            matched_items = all_cat_items

        # 2. Filter by View Mode (Logic for hiding entire category if empty)
        visible_must = []
        visible_nice = []
        
        # Process Must Have
        for item in subcats.get("Must Have", []):
            key = f"{category}_{item}"
            is_checked = st.session_state.checklist_state.get(key, False)
            
            # Filter Logic
            if view_mode == "Doar Ne-bifate" and is_checked: continue
            if search_term and search_term not in item.lower(): continue
            
            visible_must.append(item)

        # Process Nice to Have
        for item in subcats.get("Nice to Have", []):
            key = f"{category}_{item}"
            is_checked = st.session_state.checklist_state.get(key, False)
            
            # Filter Logic
            if view_mode == "Doar 'Must Have'": continue
            if view_mode == "Doar Ne-bifate" and is_checked: continue
            if search_term and search_term not in item.lower(): continue
            
            visible_nice.append(item)

        # Skip if nothing to show
        if not visible_must and not visible_nice:
            continue

        # Calculate Progress for Header
        cat_checked = sum(1 for i in all_cat_items if st.session_state.checklist_state.get(f"{category}_{i}", False))
        cat_total = len(all_cat_items)
        cat_prog = cat_checked / cat_total if cat_total > 0 else 0
        
        icon = "✅" if cat_prog == 1 else "🟦" if cat_prog > 0 else "⬜"
        
        # DISPLAY CATEGORY
        with st.expander(f"{icon} {category} ({int(cat_prog*100)}%)", expanded=(search_term != "")):
            st.progress(cat_prog)
            
            if visible_must:
                st.caption("🚨 **MUST HAVE**")
                cols = st.columns(2)
                for i, item in enumerate(visible_must):
                    key = f"{category}_{item}"
                    # Use unique key + session state logic
                    is_checked = st.session_state.checklist_state.get(key, False)
                    if cols[i%2].checkbox(item, value=is_checked, key=key):
                        st.session_state.checklist_state[key] = True
                    else:
                        st.session_state.checklist_state[key] = False
            
            if visible_must and visible_nice:
                st.markdown("---")
                
            if visible_nice:
                st.caption("✨ **NICE TO HAVE**")
                cols = st.columns(2)
                for i, item in enumerate(visible_nice):
                    key = f"{category}_{item}"
                    is_checked = st.session_state.checklist_state.get(key, False)
                    if cols[i%2].checkbox(item, value=is_checked, key=key):
                        st.session_state.checklist_state[key] = True
                    else:
                        st.session_state.checklist_state[key] = False

# --- TAB 2: SHOPPING LIST ---
with tab_shop:
    st.info("Această listă conține doar elementele NE-BIFATE. Copiază și trimite pe WhatsApp/Notes.")
    
    shopping_text = "📝 **LISTĂ CUMPĂRĂTURI CASĂ NOUĂ**\n\n"
    anything_missing = False
    
    for category, subcats in checklist_data.items():
        missing_in_cat = []
        
        # Check Must Have
        for item in subcats.get("Must Have", []):
            if not st.session_state.checklist_state.get(f"{category}_{item}", False):
                missing_in_cat.append(f"[ ] {item} (🚨)")
        
        # Check Nice to Have
        for item in subcats.get("Nice to Have", []):
            if not st.session_state.checklist_state.get(f"{category}_{item}", False):
                missing_in_cat.append(f"[ ] {item}")
                
        if missing_in_cat:
            anything_missing = True
            shopping_text += f"**{category.split(':')[0]}**:\n"
            for m in missing_in_cat:
                shopping_text += f"{m}\n"
            shopping_text += "\n"
            
    if anything_missing:
        st.text_area("Copy-Paste Text:", value=shopping_text, height=500)
    else:
        st.balloons()
        st.success("Nu ai nimic de cumpărat! Totul e bifat!")

# --- TAB 3: ANALYTICS ---
with tab_stats:
    st.header("📊 Analiză Detaliată")
    
    stats_data = []
    for category, subcats in checklist_data.items():
        all_items = subcats.get("Must Have", []) + subcats.get("Nice to Have", [])
        total = len(all_items)
        checked = sum(1 for i in all_items if st.session_state.checklist_state.get(f"{category}_{i}", False))
        percentage = (checked / total) * 100 if total > 0 else 0
        
        stats_data.append({
            "Categorie": category.split(":")[0],
            "Progres (%)": round(percentage, 1),
            "Obiecte Rămase": total - checked,
            "Total Obiecte": total
        })
        
    df_stats = pd.DataFrame(stats_data)
    
    # Sort by items remaining (descending) to show priority
    df_stats = df_stats.sort_values(by="Obiecte Rămase", ascending=False)
    
    st.bar_chart(df_stats, x="Categorie", y="Progres (%)")
    
    st.dataframe(
        df_stats.style.background_gradient(cmap="RdYlGn", subset=["Progres (%)"]),
        use_container_width=True
    )
