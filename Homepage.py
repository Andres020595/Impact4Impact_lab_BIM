import ifcopenshell
import streamlit as st

def load_predefined_ifc_file():
    # Replace 'your_predefined_file.ifc' with the path to your predefined IFC file.
    predefined_ifc_file_path = 'mad_scientist_212.ifc'
    with open(predefined_ifc_file_path, 'rb') as file:
        array_buffer = file.read()
    return array_buffer

def get_project_name():
    return session.ifc_file.by_type("IfcProject")[0].Name

def change_project_name():
    if session.project_name_input:
        session.ifc_file.by_type("IfcProject")[0].Name = session.project_name_input
        st.balloons()

def main():      
    st.set_page_config(
        layout= "wide",
        page_title="IFC Stream",
        page_icon="✍️",
    )
    st.title("Streamlit IFC")
    st.success("Predefined IFC file loaded")

    # Load the predefined IFC file
    if "array_buffer" not in session:
        session.array_buffer = load_predefined_ifc_file()
        session.ifc_file = ifcopenshell.file.from_string(session.array_buffer.decode("utf-8"))
        session.is_file_loaded = True

        ### Empty Previous Model Data from Session State
        session.isHealthDataLoaded = False
        session.HealthData = {}
        session.Graphs = {}
        session.SequenceData = {}
        session.CostScheduleData = {}

        ### Empty Previous DataFrame from Session State
        session.DataFrame = None
        session.Classes = []
        session.IsDataFrameLoaded = False

    # col1, col2 = st.columns([2, 1])
    # col1.subheader(f'Start Exploring "{get_project_name()}"')
    # col2.text_input("✏️ Change Project Name", key="project_name_input")
    # col2.button("✔️ Apply", key="change_project_name", on_click=change_project_name)

if __name__ == "__main__":
    session = st.session_state
    main()
