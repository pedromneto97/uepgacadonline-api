package com.pstwh.uepgacadonline_android.models;

/**
 * Created by pstwh on 09/07/2018.
 */

public class Documents {
    private String cpf;
    private String rg;
    private String agent;
    private String state;
    private String electionTitleNumber;
    private String electoralZone;

    public Documents(String cpf, String rg, String agent, String state, String electionTitleNumber,
                     String electoralZone) {
        this.cpf = cpf;
        this.rg = rg;
        this.agent = agent;
        this.state = state;
        this.electionTitleNumber = electionTitleNumber;
        this.electoralZone = electoralZone;
    }

    public String getCpf() {
        return cpf;
    }

    public void setCpf(String cpf) {
        this.cpf = cpf;
    }

    public String getRg() {
        return rg;
    }

    public void setRg(String rg) {
        this.rg = rg;
    }

    public String getAgent() {
        return agent;
    }

    public void setAgent(String agent) {
        this.agent = agent;
    }

    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }

    public String getElectionTitleNumber() {
        return electionTitleNumber;
    }

    public void setElectionTitleNumber(String electionTitleNumber) {
        this.electionTitleNumber = electionTitleNumber;
    }

    public String getElectoralZone() {
        return electoralZone;
    }

    public void setElectoralZone(String electoralZone) {
        this.electoralZone = electoralZone;
    }
}
