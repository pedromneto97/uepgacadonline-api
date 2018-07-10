package com.pstwh.uepgacadonline_android.helpers;

import com.pstwh.uepgacadonline_android.models.Perfil;
import com.pstwh.uepgacadonline_android.models.Person;

/**
 * Created by pstwh on 10/07/2018.
 */

public class PerfilFormHelper {

    private Perfil perfil;

    public PerfilFormHelper(Perfil perfil) {
        this.perfil = perfil;
    }

    public void setForm() {
        Person personalData = perfil.getPersonalData();


    }
}
