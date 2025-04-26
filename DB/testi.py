""" from players_crud import create_players, get_players, get_player_by_id, delete_player  # type: ignore
from events_crud import create_event, get_events, get_player_events  # type: ignore
from models import pelaaja, event
from database import get_session, create_db

# --- Alusta tietokanta ---
create_db()

session = next(get_session())

# --- Luo uusi pelaaja ---
print("\n--- Luo uusi pelaaja ---")
uusi_pelaaja = pelaaja(nimi="Keijo")
luotu_pelaaja = create_players(session, uusi_pelaaja)
print("Luotu pelaaja:", luotu_pelaaja)

# --- Hae kaikki pelaajat ---
print("\n--- Hae kaikki pelaajat ---")
kaikki_pelaajat = get_players(session)
print("Kaikki pelaajat:", kaikki_pelaajat)

# --- Hae pelaaja ID:llä ---
print("\n--- Hae pelaaja id:llä ---")
haettu_pelaaja = get_player_by_id(session, luotu_pelaaja.id)
print("Haettu pelaaja:", haettu_pelaaja)

# --- Luo eventtejä pelaajalle ---
print("\n--- Luo eventtejä pelaajalle ---")
e1 = event(type="level_started", detail="kenttä-1")
e2 = event(type="level_solved", detail="kenttä-1")

luotu_eventti1 = create_event(player_id=luotu_pelaaja.id, event_in=e1)
luotu_eventti2 = create_event(player_id=luotu_pelaaja.id, event_in=e2)

print("Luotu eventti 1:", luotu_eventti1)
print("Luotu eventti 2:", luotu_eventti2)

# --- Hae kaikki eventit ---
print("\n--- Hae kaikki eventit ---")
kaikki_eventit = get_events()
print("Kaikki eventit:", kaikki_eventit)

# --- Hae pelaajan kaikki eventit ---
print("\n--- Hae pelaajan kaikki eventit ---")
pelaajan_eventit = get_player_events(player_id=luotu_pelaaja.id)
print("Pelaajan eventit:", pelaajan_eventit)

# --- Hae eventit tyypin mukaan ---
print("\n--- Hae eventit tyypin mukaan (level_started) ---")
level_started_eventit = get_events(event_type="level_started")
print("Level started eventit:", level_started_eventit)

# --- Poista pelaaja ---
print("\n--- Poista pelaaja ---")
poisto_vastaus = delete_player(session, luotu_pelaaja.id)
print(poisto_vastaus)
 """