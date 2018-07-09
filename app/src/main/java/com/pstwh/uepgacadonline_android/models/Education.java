package com.pstwh.uepgacadonline_android.models;

/**
 * Created by pstwh on 09/07/2018.
 */

public class Education {
    private String degree;
    private String type;
    private String year;
    private String institution;
    private String course;
    private String country;
    private String state;
    private String city;

    public Education(String degree, String type, String year, String institution,
                     String course, String country, String state, String city) {
        this.degree = degree;
        this.type = type;
        this.year = year;
        this.institution = institution;
        this.course = course;
        this.country = country;
        this.state = state;
        this.city = city;
    }

    public String getDegree() {
        return degree;
    }

    public void setDegree(String degree) {
        this.degree = degree;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public String getYear() {
        return year;
    }

    public void setYear(String year) {
        this.year = year;
    }

    public String getInstitution() {
        return institution;
    }

    public void setInstitution(String institution) {
        this.institution = institution;
    }

    public String getCourse() {
        return course;
    }

    public void setCourse(String course) {
        this.course = course;
    }

    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }

    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }

    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }
}
