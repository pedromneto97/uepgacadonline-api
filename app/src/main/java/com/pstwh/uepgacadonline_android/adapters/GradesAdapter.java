package com.pstwh.uepgacadonline_android.adapters;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.TextView;

import com.pstwh.uepgacadonline_android.R;
import com.pstwh.uepgacadonline_android.models.Grade;

import java.util.List;

/**
 * Created by pstwh on 08/07/2018.
 */

public class GradesAdapter extends BaseAdapter{
    private final List<Grade> grades;
    private final Context context;


    public GradesAdapter(Context context, List<Grade> grades) {
        this.context = context;
        this.grades = grades;
    }

    @Override
    public int getCount() {
        return grades.size();
    }

    @Override
    public Object getItem(int position) {
        return grades.get(position);
    }

    @Override
    public long getItemId(int position) {
        return Long.valueOf(grades.get(position).getCod());
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        Grade grade = (Grade) getItem(position);

        LayoutInflater inflater = LayoutInflater.from(context);
        View view = inflater.inflate(R.layout.item_grade, null);

        TextView name = (TextView) view.findViewById(R.id.item_grade_name);
        name.setText(grade.getName());

        TextView absences = (TextView) view.findViewById(R.id.item_grade_absences);
        absences.setText(grade.getAbsences());

        TextView attendance = (TextView) view.findViewById(R.id.item_grade_attendance);
        attendance.setText(grade.getAttendance());

        TextView calendar = (TextView) view.findViewById(R.id.item_grade_calendar);
        calendar.setText(grade.getCalendar());

        TextView className = (TextView) view.findViewById(R.id.item_grade_class_name);
        className.setText(grade.getClassName());

        TextView cod = (TextView) view.findViewById(R.id.item_grade_cod);
        cod.setText(grade.getCod());

        TextView grade1 = (TextView) view.findViewById(R.id.item_grade_grade_1);
        grade1.setText(grade.getGrade1());

        TextView grade2 = (TextView) view.findViewById(R.id.item_grade_grade_2);
        grade2.setText(grade.getGrade2());

        TextView gradeE = (TextView) view.findViewById(R.id.item_grade_grade_e);
        gradeE.setText(grade.getGradeE());

        TextView gradeMean = (TextView) view.findViewById(R.id.item_grade_grade_mean);
        gradeMean.setText(grade.getGradeMean());

        TextView gradeStatus = (TextView) view.findViewById(R.id.item_grade_status);
        gradeStatus.setText(grade.getStatus());

        return view;
    }
}
