package com.example.natan.appnutrientes;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Spinner;
import android.widget.TextView;
import android.widget.Toast;

import java.util.ArrayList;
import java.util.List;

import javax.xml.transform.Templates;

public class MainActivity extends AppCompatActivity implements AdapterView.OnItemSelectedListener {
    EditText editNome;
    TextView textAltura;
    TextView textPeso;
    TextView dados;
    TextView necessidade_texto;
    TextView necessidade;
    TextView estilo_texto;
    Spinner spinner;
    Button  detalhes;

    String nome;
    double TMP = 0;
    double peso, altura;
    double calorias_totais = 0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        editNome = (EditText) findViewById(R.id.Nome);
        textAltura = (TextView) findViewById(R.id.Altura);
        textPeso = (TextView) findViewById(R.id.Peso);
        dados = (TextView) findViewById(R.id.dados);
        necessidade_texto = (TextView) findViewById(R.id.necessidade_texto);
        necessidade = (TextView) findViewById(R.id.necessidade);
        detalhes = (Button) findViewById(R.id.ButaoDetalhes);

        estilo_texto = (TextView) findViewById(R.id.estilo_texto);
        spinner = (Spinner) findViewById(R.id.spinner);

        spinner.setOnItemSelectedListener(this);

        List<String> categories = new ArrayList<String>();
        categories.add("Sedentário");
        categories.add("Levemente ativo");
        categories.add("Moderadamente ativo");
        categories.add("Muito ativo");

        ArrayAdapter<String> dataAdapter = new ArrayAdapter<String>(this, android.R.layout.simple_spinner_item, categories);

        dataAdapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);

        spinner.setAdapter(dataAdapter);
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
                altura = data.getDoubleExtra("Altura",0);
                peso = data.getDoubleExtra("Peso", 0);
                nome = data.getStringExtra("Nome");
                textAltura.setText(String.format("Altura: %s m", Double.toString(altura)));
                textAltura.setVisibility(View.VISIBLE);
                textPeso.setText(String.format("Peso: %s kg", Double.toString(peso)));
                textPeso.setVisibility(View.VISIBLE);
                dados.setText(String.format("Dados de %s", nome));
                dados.setVisibility(View.VISIBLE);
                editNome.getText().clear();
                TMP = (11.3 * peso) + (16 * altura) + 901;
                necessidade_texto.setVisibility(View.VISIBLE);
                necessidade.setVisibility(View.VISIBLE);
                spinner.setVisibility(View.VISIBLE);
                estilo_texto.setVisibility(View.VISIBLE);
                detalhes.setVisibility(View.VISIBLE);
                calorias_totais = TMP;
                necessidade.setText(String.format("%.2f Calorias", calorias_totais));

            }
        }

    }

    @Override
    public void onItemSelected(AdapterView<?> parent, View view, int position, long id) {
        // On selecting a spinner item
        String item = parent.getItemAtPosition(position).toString();
        switch (item){
            case "Sedentário":
                calorias_totais = TMP;
                necessidade.setText(String.format("%.2f Calorias", calorias_totais));
                break;
            case "Levemente ativo":
                calorias_totais = TMP * 1.11;
                necessidade.setText(String.format("%.2f Calorias", calorias_totais));
                break;
            case "Moderadamente ativo":
                calorias_totais = TMP * 1.25;
                necessidade.setText(String.format("%.2f Calorias", calorias_totais));
                break;
            case "Muito ativo":
                calorias_totais = TMP * 1.48;
                necessidade.setText(String.format("%.2f Calorias",calorias_totais));
                break;
        }

        // Showing selected spinner item
        Toast.makeText(parent.getContext(), "Selected: " + item, Toast.LENGTH_LONG).show();
    }

    @Override
    public void onNothingSelected(AdapterView<?> parent) {

    }

    public void nes_cal_det(View view) {
        final Intent intent = new Intent(this, NecessidadeDetalhadasActivity.class);
        intent.putExtra("Nome", nome);
        intent.putExtra("CaloriasTotais", calorias_totais);
        startActivity(intent);
    }
}
