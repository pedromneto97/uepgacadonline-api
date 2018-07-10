package com.pstwh.uepgacadonline_android.helpers;

import android.widget.EditText;

import com.pstwh.uepgacadonline_android.PerfilActivity;
import com.pstwh.uepgacadonline_android.R;
import com.pstwh.uepgacadonline_android.models.Perfil;

/**
 * Created by pstwh on 10/07/2018.
 */

public class PerfilFormHelper {

    private final EditText academicRegister;
    private final EditText completeName;
    private final EditText socialName;
    private final EditText genre;
    private final EditText socialGenre;
    private final EditText birthDate;
    private final EditText nationality;
    private final EditText birthState;
    private final EditText birthCity;
    private final EditText birthCountry;
    private final EditText fatherName;
    private final EditText motherName;
    private final EditText cep;
    private final EditText address;
    private final EditText addressNumber;
    private final EditText complement;
    private final EditText neighborhood;
    private final EditText city;
    //private final EditText state;
    //private final EditText telephone;
    private final EditText lattes;
    private final EditText email;
    private final EditText cpf;
    private final EditText rg;
    private final EditText documentAgent;
    private final EditText documentState;
    private final EditText electionTitleNumber;
    private final EditText electoralZone;
    private final EditText number;
    private final EditText category;
    private final EditText agent;
    private final EditText date;
    private final EditText degree;
    private final EditText type;
    private final EditText year;
    private final EditText institution;
    private final EditText course;
    private final EditText institutionCountry;
    private final EditText institutionState;
    private final EditText institutionCity;


    public PerfilFormHelper(PerfilActivity activity) {
        academicRegister = (EditText) activity.findViewById(R.id.perfil_ra_edit_text);
        completeName = (EditText) activity.findViewById(R.id.perfil_complet_name_edit_text);
        socialName = (EditText) activity.findViewById(R.id.perfil_social_name_edit_text);
        genre = (EditText) activity.findViewById(R.id.perfil_genre_name_edit_text);
        socialGenre = (EditText) activity.findViewById(R.id.perfil_social_genre_edit_text);
        birthDate = (EditText) activity.findViewById(R.id.perfil_birth_date_edit_text);
        nationality = (EditText) activity.findViewById(R.id.perfil_nationality_edit_text);
        birthState = (EditText) activity.findViewById(R.id.perfil_birth_state_edit_text);
        birthCity = (EditText) activity.findViewById(R.id.perfil_birth_city_edit_text);
        birthCountry = (EditText) activity.findViewById(R.id.perfil_birth_country_edit_text);
        fatherName = (EditText) activity.findViewById(R.id.perfil_father_name_edit_text);
        motherName = (EditText) activity.findViewById(R.id.perfil_mother_name_edit_text);
        cep = (EditText) activity.findViewById(R.id.perfil_cep_edit_text);
        address = (EditText) activity.findViewById(R.id.perfil_address_edit_text);
        addressNumber = (EditText) activity.findViewById(R.id.perfil_number_edit_text);
        complement = (EditText) activity.findViewById(R.id.perfil_complement_edit_text);
        neighborhood = (EditText) activity.findViewById(R.id.perfil_neighborhood_edit_text);
        city = (EditText) activity.findViewById(R.id.perfil_city_edit_text);
        //state = (EditText) activity.findViewById(R.id.perfil_state_edit_text);
        //telephone = (EditText) activity.findViewById(R.id.perfil_telephone_edit_text);
        lattes = (EditText) activity.findViewById(R.id.perfil_lattes_edit_text);
        email = (EditText) activity.findViewById(R.id.perfil_email_edit_text);
        cpf = (EditText) activity.findViewById(R.id.perfil_cpf_edit_text);
        rg = (EditText) activity.findViewById(R.id.perfil_rg_edit_text);
        documentAgent = (EditText) activity.findViewById(R.id.perfil_agent_edit_text);
        documentState = (EditText) activity.findViewById(R.id.perfil_doc_state_edit_text);
        electionTitleNumber = (EditText) activity.findViewById(R.id.perfil_zone_number_edit_text);
        electoralZone = (EditText) activity.findViewById(R.id.perfil_zone_edit_text);
        number = (EditText) activity.findViewById(R.id.perfil_militar_document_numer_edit_text);
        category = (EditText) activity.findViewById(R.id.perfil_militar_category_edit_text);
        agent = (EditText) activity.findViewById(R.id.perfil_militar_agent_edit_text);
        date = (EditText) activity.findViewById(R.id.perfil_militar_doc_date_edit_text);
        degree = (EditText) activity.findViewById(R.id.perfil_degree_edit_text);
        type = (EditText) activity.findViewById(R.id.perfil_type_edit_text);
        year = (EditText) activity.findViewById(R.id.perfil_year_edit_text);
        institution = (EditText) activity.findViewById(R.id.perfil_institution_edit_text);
        course = (EditText) activity.findViewById(R.id.perfil_course_edit_text);
        institutionCountry = (EditText) activity.findViewById(R.id.perfil_education_country_edit_text);
        institutionState = (EditText) activity.findViewById(R.id.perfil_education_state_edit_text);
        institutionCity = (EditText) activity.findViewById(R.id.perfil_education_city_edit_text);
    }

    public void setPerfil(Perfil perfil) {
        academicRegister.setText(perfil.getAcademicRegister());
        completeName.setText(perfil.getCompleteName());
        socialName.setText(perfil.getSocialName());
        genre.setText(perfil.getGenre());
        socialGenre.setText(perfil.getSocialGenre());
        birthDate.setText(perfil.getBirthDate());
        nationality.setText(perfil.getNationality());
        birthState.setText(perfil.getBirthState());
        birthCity.setText(perfil.getBirthCity());
        birthCountry.setText(perfil.getBirthCountry());
        fatherName.setText(perfil.getFatherName());
        motherName.setText(perfil.getMotherName());
        cep.setText(perfil.getCep());
        address.setText(perfil.getAddress());
        addressNumber.setText(perfil.getAddressNumber());
        complement.setText(perfil.getComplement());
        neighborhood.setText(perfil.getNeighborhood());
        city.setText(perfil.getCity());
        //state.setText(perfil.getState());
        //telephone.setText(perfil.getTelephone());
        lattes.setText(perfil.getLattes());
        email.setText(perfil.getEmail());
        cpf.setText(perfil.getCpf());
        rg.setText(perfil.getRg());
        documentAgent.setText(perfil.getDocumentAgent());
        documentState.setText(perfil.getDocumentState());
        electionTitleNumber.setText(perfil.getElectionTitleNumber());
        electoralZone.setText(perfil.getElectoralZone());
        number.setText(perfil.getNumber());
        category.setText(perfil.getCategory());
        agent.setText(perfil.getAgent());
        date.setText(perfil.getDate());
        degree.setText(perfil.getDegree());
        type.setText(perfil.getType());
        year.setText(perfil.getYear());
        institution.setText(perfil.getInstitution());
        course.setText(perfil.getCourse());
        institutionCountry.setText(perfil.getInstitutionCountry());
        institutionState.setText(perfil.getInstitutionState());
        institutionCity.setText(perfil.getInstitutionCity());
    }


}
