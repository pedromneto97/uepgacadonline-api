package com.pstwh.uepgacadonline_android.models;

/**
 * Created by pstwh on 08/07/2018.
 */

public class Grade {
    private String cod;
    private String name;
    private String className;
    private String calendar;
    private String absences;
    private String grade1;
    private String grade2;
    private String gradeE;
    private String gradeMean;
    private String attendance;
    private String status;

    public Grade(String cod, String name, String className, String calendar, String absences,
                 String grade1, String grade2, String gradeE, String gradeMean, String attendance,
                 String status) {
        this.cod = cod;
        this.name = name;
        this.className = className;
        this.calendar = calendar;
        this.absences = absences;
        this.grade1 = grade1;
        this.grade2 = grade2;
        this.gradeE = gradeE;
        this.gradeMean = gradeMean;
        this.attendance = attendance;
        this.status = status;
    }

    public String getCod() {
        return cod;
    }

    public void setCod(String cod) {
        this.cod = cod;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getClassName() {
        return className;
    }

    public void setClassName(String className) {
        this.className = className;
    }

    public String getCalendar() {
        return calendar;
    }

    public void setCalendar(String calendar) {
        this.calendar = calendar;
    }

    public String getAbsences() {
        return absences;
    }

    public void setAbsences(String absences) {
        this.absences = absences;
    }

    public String getGrade1() {
        return grade1;
    }

    public void setGrade1(String grade1) {
        this.grade1 = grade1;
    }

    public String getGrade2() {
        return grade2;
    }

    public void setGrade2(String grade2) {
        this.grade2 = grade2;
    }

    public String getGradeE() {
        return gradeE;
    }

    public void setGradeE(String gradeE) {
        this.gradeE = gradeE;
    }

    public String getGradeMean() {
        return gradeMean;
    }

    public void setGradeMean(String gradeMean) {
        this.gradeMean = gradeMean;
    }

    public String getAttendance() {
        return attendance;
    }

    public void setAttendance(String attendance) {
        this.attendance = attendance;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
}
