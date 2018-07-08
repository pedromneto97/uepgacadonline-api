package com.pstwh.uepgacadonline_android;

import android.content.Intent;
import android.os.Bundle;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.LinearLayout;
import android.widget.ListView;
import android.widget.TableLayout;
import android.widget.TableRow;
import android.widget.TextView;
import android.widget.Toast;

import com.pstwh.uepgacadonline_android.adapters.GradesAdapter;
import com.pstwh.uepgacadonline_android.models.Grade;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.concurrent.ExecutionException;

public class GradeActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_grade);

        Intent intent = getIntent();
        UepgWrapper uepg = (UepgWrapper) intent.getSerializableExtra("uepg");

        ListView gradeList = (ListView) findViewById(R.id.list_view_grade);

        try {
            List<Grade> grades = uepg.getGrade();

            System.out.println(grades);

            GradesAdapter adapter = new GradesAdapter(this, grades);
            gradeList.setAdapter(adapter);

        } catch (Exception e) {
            Toast.makeText(GradeActivity.this, "Usuário ou senha inválidos!", Toast.LENGTH_LONG).show();
            finish();
        }

        /*
        try {
            ArrayList<ArrayList<String>> grades = uepg.getGrade();

            TableLayout table = (TableLayout) findViewById(R.id.grade_table_layout);

            for(ArrayList<String> grade : grades) {
                TableRow row = new TableRow(this);

                for(String col : grade) {
                    TextView col_tv = new TextView(this);
                    col_tv.setText(col);
                    row.addView(col_tv);
                }

                table.addView(row);
            }
        } catch (InterruptedException e) {
            e.printStackTrace();
        } catch (ExecutionException e) {
            e.printStackTrace();
        }
        */


        /*
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        FloatingActionButton fab = (FloatingActionButton) findViewById(R.id.fab);
        fab.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Snackbar.make(view, "Replace with your own action", Snackbar.LENGTH_LONG)
                        .setAction("Action", null).show();
            }
        });

        */

    }

}
