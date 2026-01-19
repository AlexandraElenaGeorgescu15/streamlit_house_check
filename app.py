import streamlit as st
import json

# --- 1. CONFIGURARE PAGINĂ ---
st.set_page_config(
    page_title="Checklist Mutare: Ultimate Edition",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. DATELE COMPLETE (Sursă: PDF Original + Life Hacks + Modern Tech) ---
checklist_data = {
    "🍳 Bucătărie: Electrocasnice (Appliances)": {
        "Must Have": [
            "1. Aparat cafea / Presă franceză", "2. Fierbător apă (Kettle)", "3. Cuptor microunde", 
            "4. Prăjitor pâine", "36. Foarfecă bucătărie", "39. Deschizător conserve",
            "35. Bol salată", "43. Wok", "32. Oale și tigăi (Set)", "16. Vas Casserole"
        ],
        "Nice to Have": [
            "5. Blender", "6. Formă brioșe (Cupcake tray)", "7. Cântar bucătărie", 
            "26. Storcător fructe (Juice extractor)", 
            "Air Fryer (Gătit rapid & sănătos)", 
            "SodaStream (Adio cărat apă)",
            "Aparat vidat alimente (Păstrează mâncarea proaspătă)"
        ]
    },
    "🔪 Bucătărie: Ustensile & Gătit": {
        "Must Have": [
            "8. Linguri măsurat", "9. Cană gradată", "10. Boluri mixare", "11. Făcăleț", 
            "12. Sită (Sieve)", "13. Tel (Whisk)", "15. Deschizător sticle", "17. Răzătoare", 
            "19. Tocătoare (Chopping boards)", "20. Strecurătoare (Colander)", "21. Tirbușon", 
            "31. Deschizător conserve (Tin opener)", "37. Spatulă", "40. Clește (Tongs)", 
            "41. Curățător legume (Peeler)", "44. Linguri de lemn", "34. Zdrobitor cartofi",
            "24. Paletă pește (Fish slice)", "25. Presă usturoi"
        ],
        "Nice to Have": [
            "14. Grătar răcire prăjituri", "18. Feliator brânză", "22. Pahare ouă", 
            "23. Timer ouă", "27. Capac microunde", "28. Tăvi cuptor", "30. Feliator pizza",
            "31. Tavă pizza", "33. Suport oale fierbinți", "50. Lingură înghețată", 
            "52. Polonic", 
            "Ascuțitor electric cuțite (Life Hack)",
            "Organizator capace oale (Anti-Haos)"
        ]
    },
    "🍽️ Bucătărie: Servire & Organizare": {
        "Must Have": [
            "45. Boluri", "48. Furculițe (Masă & Desert)", "49. Pahare", 
            "51. Cuțite (Unt, Steak, Chefi)", "54. Căni (Mugs)", "55. Farfurii (Întinse & Desert)", 
            "56. Linguri (Supă, Desert, Ceai)", "63. Cutie pâine", "64. Suport tacâmuri sertar", 
            "66. Tablete mașină spălat vase", "67. Scurgător vase", "79. Lichid vase", 
            "73. Sită scurgere chiuvetă", "70. Suport prosoape hârtie", "71. Solnițe sare/piper"
        ],
        "Nice to Have": [
            "38. Zaharniță", "42. Sticlă apă", "46. Suporturi pahare (Coasters)", 
            "47. Shaker cocktail", "53. Cană lapte", "57. Ceainic", "58. Tavă servire", 
            "59. Carafă apă", "60. Frapieră (Wine cooler)", "61. Pahare vin", 
            "69. Tavă cuburi gheață", "68. Coș fructe", "74. Raft condimente", 
            "75. Organizator chiuvetă (Caddy)", "80. Suport vin", 
            "Organizator rotativ (Lazy Susan)", "Lumini LED sub dulapuri (Pentru blat)"
        ]
    },
    "🧤 Bucătărie: Textile & Consumabile": {
        "Must Have": [
            "82. Prosoape hârtie", "85. Prosoape bucătărie (Textil)", "84. Mănuși cuptor", 
            "72. Pungi sandwich", "77. Folie aluminiu", "65. Folie alimentară", 
            "78. Caserole (Tupperware)"
        ],
        "Nice to Have": [
            "81. Șorț", "83. Șervețele masă (Napkins)", "76. Cutie ceai", 
            "Etichetator (Label Maker)"
        ]
    },
    "🛁 Baie: Esențiale": {
        "Must Have": [
            "90. Perie WC", "89. Pompă desfundat (Plunger)", "86. Perdea duș", "87. Covoraș duș", 
            "98. Hârtie igienică", "91. Dozator săpun", "92. Suport prosoape", 
            "94. Prosoape baie (mari)", "96. Prosoape mâini", 
            "Racletă duș (Squeegee - 162 in cleaning list, dar critic aici)"
        ],
        "Nice to Have": [
            "88. Etajeră duș", "93. Cântar corporal", "95. Prosoape față", "97. Șervețele cutie", 
            "62. Lighean (Basin)", "Covoraș Diatomit (Uscare instantă)", 
            "Capac WC Bideu / Duș igienic"
        ]
    },
    "🛏️ Dormitor & Textile": {
        "Must Have": [
            "100. Cearșafuri pat", "101. Husă pilotă", "102. Protecție saltea", 
            "103. Fețe pernă", "105. Pilotă", "106. Perne", "107. Suport pantofi"
        ],
        "Nice to Have": [
            "99. Cuvertură pat (Bed spread)", "104. Protecții perne", 
            "Topper Saltea Memory Foam", "Lumini senzor dulap haine", 
            "Draperii Blackout (Somn mai bun)"
        ]
    },
    "🧺 Spălătorie & Îngrijire Haine": {
        "Must Have": [
            "108. Uscător rufe (Stander)", "110. Fier de călcat", "111. Masă de călcat", 
            "113. Coșuri rufe", "114. Detergent rufe (Powder/Liquid)", "115. Umerașe"
        ],
        "Nice to Have": [
            "109. Bile uscător / Șervețele uscător", "112. Sac spălare delicate", 
            "116. Trusă cusut", 
            "Steamer Vertical (Călcat rapid fără masă)", 
            "Aparat curățat scame (Lint Remover)",
            "Umerașe catifea (Antiderapante)"
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
            "129. Plante", "130. Vază", 
            "Lampă veghe cu senzor (Hol/Baie)"
        ]
    },
    "🧹 Curățenie (Cleaning Essentials)": {
        "Must Have": [
            "147. Clor/Înălbitor", "148. Soluție baie", "149. Dezinfectant", "152. Soluție universală", 
            "153. Soluție geamuri", "154. Saci menajeri (Bin bags)", "155. Coșuri gunoi (Bins)", 
            "156. Găleată și Mop", "158. Lavete/Cârpe", "160. Mănuși cauciuc", 
            "163. Făraș", "164. Mătură", "165. Aspirator"
        ],
        "Nice to Have": [
            "150. Soluție pete covoare", "151. Soluție cuptor", "157. Coș produse (Caddy)", 
            "159. Pămătuf praf", "161. Perii frecat", 
            "Robot Aspirator (cu stație golire)", 
            "Mop cu pulverizator (Spray Mop)",
            "Perie electrică rotativă (Spin Scrubber)"
        ]
    },
    "🌳 Grădină & Exterior (Outdoor)": {
        "Must Have": [
            "136. Mașină tuns iarba", "135. Furtun apă", "143. Mătură curte", 
            "145. Frânghie rufe", "146. Cârlige rufe"
        ],
        "Nice to Have": [
            "131. Grătar (BBQ)", "132. Ustensile BBQ", "133. Mănuși grădinărit", 
            "134. Scaunel grădinărit", "137. Coș cârlige", "138. Foarfecă pomi (Pruners)", 
            "139. Greblă", "140. Foarfecă mare (Shears)", "141. Mistrie", "142. Stropitoare", 
            "144. Lacăt magazie"
        ]
    },
    "🛠️ Bricolaj (DIY & Improvement)": {
        "Must Have": [
            "171. Cutter", "172. Bormașină", "173. Ciocan", "174. Ruletă măsurat", 
            "175. Clește", "176. Șurubelnițe", "177. Bandă adezivă", "178. Trusă scule", 
            "179. Lanternă", "182. Scară pliantă"
        ],
        "Nice to Have": [
            "166. Pensule vopsit", "167. Folie protecție vopsea", "168. Trafalet", 
            "169. Șpaclu (Scraper)", "170. Tavă vopsea", "180. Protecții pâslă mobilă", 
            "181. Rafturi/Polițe", "183. Cutii depozitare", "184. Cârlige perete",
            "Cheie aerisit calorifere (Critic)", "WD-40 Siliconic (Termopane)"
        ]
    },
    "🔥 Siguranță & Sănătate (Health & Safety)": {
        "Must Have": [
            "185. Detector monoxid carbon", "186. Detector fum", "189. Trusă prim ajutor", 
            "192. Baterii", "195. Prelungitor", "200. WD40 (Clasic)", "201. Covoraș intrare",
            "Termometru corporal", "Medicamente bază"
        ],
        "Nice to Have": [
            "187. Pătură ignifugă", "188. Stingător incendiu", "190. Alarmă securitate", 
            "191. Cameră securitate", "193. Cuier haine", "194. Opritor ușă", 
            "196. Suport chei", "197. Chibrituri/Brichetă", "198. Scotch (Sellotape)", 
            "199. Suport umbrele", 
            "DEZUMIDIFICATOR (Game Changer)", 
            "Purificator Aer", "Higrometru (Măsoară umiditatea)"
        ]
    },
    "🖥️ Home Office & Tech (Nou)": {
        "Must Have": [
            "Birou lucru", "Scaun ergonomic", "Monitor extern", "Prelungitor cu protecție", 
            "Laptop/PC", "Cabluri încărcare"
        ],
        "Nice to Have": [
            "Lampă birou", "Suport Laptop/Monitor", "Tastatură & Mouse", "Webcam", 
            "Imprimantă/Scanner", "Distrugător documente", 
            "Priză turn/Cub cu USB-C", "Sistem Mesh Wi-Fi"
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

# --- 3. CALCUL TOTALURI ---
def count_items(data):
    total = 0
    for cat in data.values():
        total += len(cat.get("Must Have", [])) + len(cat.get("Nice to Have", []))
    return total

total_items = count_items(checklist_data)

# --- 4. GESTIONAREA STĂRII ---
if 'checklist_state' not in st.session_state:
    st.session_state.checklist_state = {}

def reset_checklist():
    st.session_state.checklist_state = {}

# --- 5. INTERFAȚA ---

st.title(f"📦 Checklist Mutare: {total_items} Articole")
st.markdown("""
**Lista Completă.** Include cele 201 articole originale, plus **Life Hacks** (Dezumidificator, Steamer, etc.) pentru o viață mai ușoară.
""")

# -- Sidebar --
with st.sidebar:
    st.header("⚙️ Control")
    checked = sum(1 for v in st.session_state.checklist_state.values() if v)
    st.metric("Progres", f"{checked} / {total_items}")
    st.progress(checked / total_items if total_items > 0 else 0)
    
    st.markdown("---")
    st.download_button("📥 Descarcă JSON", json.dumps(st.session_state.checklist_state), "checklist_ultimate.json")
    
    if st.button("🗑️ Resetare Completă"):
        reset_checklist()
        st.rerun()

# -- Afișare Categorii --
for cat_name, subcats in checklist_data.items():
    items_in_cat = subcats.get("Must Have", []) + subcats.get("Nice to Have", [])
    if not items_in_cat: continue
        
    cat_checked = sum(1 for i in items_in_cat if st.session_state.checklist_state.get(f"{cat_name}_{i}", False))
    cat_total = len(items_in_cat)
    state_icon = "✅" if cat_checked == cat_total else "🟦"
    if cat_checked == 0: state_icon = "⬜"

    # Auto-expand dacă categoria e începută sau critică
    auto_expand = False
    if cat_checked > 0 and cat_checked < cat_total:
        auto_expand = True
    if "Sănătate" in cat_name or "Home Office" in cat_name:
        auto_expand = True

    with st.expander(f"{state_icon} {cat_name} ({cat_checked}/{cat_total})", expanded=auto_expand):
        
        if subcats.get("Must Have"):
            st.markdown("##### 🚨 Must Have")
            cols = st.columns(2)
            for i, item in enumerate(subcats["Must Have"]):
                key = f"{cat_name}_{item}"
                if cols[i%2].checkbox(item, value=st.session_state.checklist_state.get(key, False), key=key):
                    st.session_state.checklist_state[key] = True
                else:
                    st.session_state.checklist_state[key] = False
        
        if subcats.get("Nice to Have"):
            st.markdown("##### ✨ Nice to Have / Life Hacks")
            cols = st.columns(2)
            for i, item in enumerate(subcats["Nice to Have"]):
                key = f"{cat_name}_{item}"
                if cols[i%2].checkbox(item, value=st.session_state.checklist_state.get(key, False), key=key):
                    st.session_state.checklist_state[key] = True
                else:
                    st.session_state.checklist_state[key] = False
