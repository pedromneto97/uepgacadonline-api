package com.pstwh.uepgacadonline_android.models;

/**
 * Created by pstwh on 09/07/2018.
 */

public class MilitarSituation {
    private String number;
    private String category;
    private String agent;
    private String date;

    public MilitarSituation(String number, String category, String agent, String date) {
        this.number = number;
        this.category = category;
        this.agent = agent;
        this.date = date;
    }

    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }

    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }

    public String getAgent() {
        return agent;
    }

    public void setAgent(String agent) {
        this.agent = agent;
    }

    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
}
