package com.pstwh.uepgacadonline_android.models;

/**
 * Created by pstwh on 09/07/2018.
 */

public class Person {

    private String cod;
    private String completeName;
    private String socialName;
    private String genre;
    private String socialGenre;
    private String birthDate;
    private String nationality;
    private String birthState;
    private String birthCity;
    private String birthCountry;
    private String fatherName;
    private String motherName;

    public Person(String cod, String completeName, String socialName, String genre,
                  String socialGenre, String birthDate, String nationality, String birthState,
                  String birthCity, String birthCountry, String fatherName, String motherName) {
        this.cod = cod;
        this.completeName = completeName;
        this.socialName = socialName;
        this.genre = genre;
        this.socialGenre = socialGenre;
        this.birthDate = birthDate;
        this.nationality = nationality;
        this.birthState = birthState;
        this.birthCity = birthCity;
        this.birthCountry = birthCountry;
        this.fatherName = fatherName;
        this.motherName = motherName;
    }

    public String getCod() {
        return cod;
    }

    public void setCod(String cod) {
        this.cod = cod;
    }

    public String getCompleteName() {
        return completeName;
    }

    public void setCompleteName(String completeName) {
        this.completeName = completeName;
    }

    public String getSocialName() {
        return socialName;
    }

    public void setSocialName(String socialName) {
        this.socialName = socialName;
    }

    public String getGenre() {
        return genre;
    }

    public void setGenre(String genre) {
        this.genre = genre;
    }

    public String getSocialGenre() {
        return socialGenre;
    }

    public void setSocialGenre(String socialGenre) {
        this.socialGenre = socialGenre;
    }

    public String getBirthDate() {
        return birthDate;
    }

    public void setBirthDate(String birthDate) {
        this.birthDate = birthDate;
    }

    public String getNationality() {
        return nationality;
    }

    public void setNationality(String nationality) {
        this.nationality = nationality;
    }

    public String getBirthState() {
        return birthState;
    }

    public void setBirthState(String birthState) {
        this.birthState = birthState;
    }

    public String getBirthCity() {
        return birthCity;
    }

    public void setBirthCity(String birthCity) {
        this.birthCity = birthCity;
    }

    public String getBirthCountry() {
        return birthCountry;
    }

    public void setBirthCountry(String birthCountry) {
        this.birthCountry = birthCountry;
    }

    public String getFatherName() {
        return fatherName;
    }

    public void setFatherName(String fatherName) {
        this.fatherName = fatherName;
    }

    public String getMotherName() {
        return motherName;
    }

    public void setMotherName(String motherName) {
        this.motherName = motherName;
    }
}
