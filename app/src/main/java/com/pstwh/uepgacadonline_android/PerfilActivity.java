package com.pstwh.uepgacadonline_android;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

import com.pstwh.uepgacadonline_android.models.Perfil;

import java.util.concurrent.ExecutionException;

public class PerfilActivity extends AppCompatActivity {

    public UepgWrapper uepg;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_perfil);

        Intent intent = getIntent();
        uepg = (UepgWrapper) intent.getSerializableExtra("uepg");

        try {
            Perfil p = uepg.getPerfil();
        } catch (ExecutionException e) {
            e.printStackTrace();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
