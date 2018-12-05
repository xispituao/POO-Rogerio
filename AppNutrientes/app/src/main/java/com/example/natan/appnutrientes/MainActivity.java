package com.example.natan.appnutrientes;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;

import javax.xml.transform.Templates;

public class MainActivity extends AppCompatActivity {
    EditText editNome;
    TextView textAltura;
    TextView textPeso;
    TextView dados;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        editNome = (EditText) findViewById(R.id.Nome);
        textAltura = (TextView) findViewById(R.id.Altura);
        textPeso = (TextView) findViewById(R.id.Peso);
        dados = (TextView) findViewById(R.id.dados);
    }

    public void dados(View view) {
        String nome = editNome.getText().toString();
        final Intent intent = new Intent(this, DadosActivity.class);
        intent.putExtra("Nome", nome);
        startActivityForResult(intent,1);
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data){
        super.onActivityResult(requestCode, resultCode, data);

        if (requestCode == 1){
            if (resultCode == RESULT_OK){
                int altura = data.getIntExtra("Altura",0);
                double peso = data.getDoubleExtra("Peso", 0);
                textAltura.setText(Integer.toString(altura));
                textAltura.setVisibility(View.VISIBLE);
                textPeso.setText(Double.toString(peso));
                textPeso.setVisibility(View.VISIBLE);
                dados.setVisibility(View.VISIBLE);
                editNome.getText().clear();

            }
        }

    }
}
