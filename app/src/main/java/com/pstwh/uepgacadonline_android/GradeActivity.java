package com.pstwh.uepgacadonline_android;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.widget.ListView;
import android.widget.Toast;

import com.pstwh.uepgacadonline_android.adapters.GradesAdapter;
import com.pstwh.uepgacadonline_android.models.Grade;

import java.util.List;

public class GradeActivity extends AppCompatActivity {

    public UepgWrapper uepg;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_grade);

        Intent intent = getIntent();
        uepg = (UepgWrapper) intent.getSerializableExtra("uepg");

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
    }
/*
    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        MenuInflater inflater = getMenuInflater();
        inflater.inflate(R.menu.menu_grades, menu);

        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        switch (item.getItemId()) {
            case R.id.menu_item_documentos:
                Intent documents = new Intent(GradeActivity.this, DocumentActivity.class);
                documents.putExtra("uepg", uepg);
                startActivity(documents);
                break;
        }

        return super.onOptionsItemSelected(item);
    }
    */
}
