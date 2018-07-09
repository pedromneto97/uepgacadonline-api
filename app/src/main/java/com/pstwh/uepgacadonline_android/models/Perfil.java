package com.pstwh.uepgacadonline_android.models;

/**
 * Created by pstwh on 09/07/2018.
 */

public class Perfil {
    private Person personalData;
    private Address address;
    private Documents documents;
    private MilitarSituation militarSituation;
    private Education education;

    public Perfil(Person personalData, Address address, Documents documents,
                  MilitarSituation militarSituation, Education education) {
        this.personalData = personalData;
        this.address = address;
        this.documents = documents;
        this.militarSituation = militarSituation;
        this.education = education;
    }

    public Person getPersonalData() {
        return personalData;
    }

    public void setPersonalData(Person personalData) {
        this.personalData = personalData;
    }

    public Address getAddress() {
        return address;
    }

    public void setAddress(Address address) {
        this.address = address;
    }

    public Documents getDocuments() {
        return documents;
    }

    public void setDocuments(Documents documents) {
        this.documents = documents;
    }

    public MilitarSituation getMilitarSituation() {
        return militarSituation;
    }

    public void setMilitarSituation(MilitarSituation militarSituation) {
        this.militarSituation = militarSituation;
    }

    public Education getEducation() {
        return education;
    }

    public void setEducation(Education education) {
        this.education = education;
    }
}
