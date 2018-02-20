import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import plotly
from plotly.graph_objs import *
from plotly.offline import download_plotlyjs, plot
from collections import defaultdict
import pandas as pd
import sys
container= {
    'display':'grid',
    'grid-template-columns':'repeat(2, 1fr)',
    'grid-template-rows':'repeat(2, minmax(100px, auto))',
    'grid-padding': '1em',
}
app = dash.Dash(__name__)
server = app.server
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})
colors={
'background':'#7FDBFF',
'test':'11111111'
}
app.config.suppress_callback_exceptions=True
df = pd.read_csv('https://raw.githubusercontent.com/azharz4u/checking/master/KPI_overview.csv')
availableRNCname= df['RNC name'].unique()
app.layout = html.Div([
html.Div([
dcc.Dropdown(
id='mydropdown',
options=[{'label': i, 'value': i} for i in availableRNCname],
value=['N104', 'N103','N105','N110','N119'],
multi=True),
html.Div([
html.H1('RRC Connection setup SR'),
dcc.Graph(id='graph0'),
],style={'background':'#7FDBFF','display': 'inline-block', 'width': '49%','height': '70%'}),
html.Div([
html.H1('Call Setup Success Rate CS -Speech'),
dcc.Graph(id='graph1')
],style={'background':'#7FDBFF','background':'#7FDBFF','display': 'inline-block', 'width': '49%'}),
html.Div([
html.H1('HSDPA Accessibility'),
dcc.Graph(
id='graph2',
)
],style={'background':'#7FDBFF','display': 'inline-block', 'width': '49%'}),
html.Div([
html.H1('HSUPA Accessibility'),
dcc.Graph(
id='graph3')
],style={'background':'#7FDBFF','display': 'inline-block', 'width': '49%'}),
html.Div([
html.H1('CSSR for PS'),
dcc.Graph(
id='graph4')
],style={'background':'#7FDBFF','display': 'inline-block', 'width': '49%'}),
html.Div([
html.H1('Soft Handover Success Rate CS and PS'),
dcc.Graph(
id='graph5')
],style={'background':'#7FDBFF','display': 'inline-block', 'width': '49%'}),
html.Div([
html.H1('IRAT HO Success Rate CS'),
dcc.Graph(
id='graph6')
],style={'background':'#7FDBFF','display': 'inline-block', 'width': '49%'}),
html.Div([
html.H1('3G Traffic CS - Speech'),
dcc.Graph(
id='graph7')
],style={'background':'#7FDBFF','display': 'inline-block', 'width': '49%'}),
html.Div([
html.H1('PS HSUPA Volume'),
dcc.Graph(
id='graph8')
],style={'background':'#7FDBFF','display': 'inline-block', 'width': '49%'}),
html.Div([
html.H1('PS HSDPA Volume'),
dcc.Graph(
id='graph9')
],style={'background':'#7FDBFF','display': 'inline-block', 'width': '49%'}),
html.Div([
html.H1('AVG Nbr of HSDPA Users'),
dcc.Graph(
id='graph10')
],style={'background':'#7FDBFF','display': 'inline-block', 'width': '49%'}),html.Div([
html.H1('AVG Nbr of HSUPA Users'),
dcc.Graph(
id='graph11')
],style={'background':'#7FDBFF','display': 'inline-block', 'width': '49%'}),
html.Div([
html.H1('CS drop rate'),
dcc.Graph(
id='graph12')
],style={'background':'#7FDBFF','display': 'inline-block', 'width': '49%'}),

html.Div([
html.H1('PS Global RAB Drop Rate'),
dcc.Graph(
id='graph13')
],style={'background':'#7FDBFF','display': 'inline-block', 'width': '49%'}),
html.Div([
html.H1('PS HSDPA RAB Drop Rate'),
dcc.Graph(
id='graph14')
],style={'background':'#7FDBFF','display': 'inline-block', 'width': '49%'}),
html.Div([
html.H1('PS HSUPA RAB Drop Rate'),
dcc.Graph(
id='graph15')
],style={'background':'#7FDBFF','display': 'inline-block', 'width': '49%'}),
html.Div([
html.H1('PS HSDPA Throughput'),
dcc.Graph(
id='graph16')
],style={'background':'#7FDBFF','display': 'inline-block', 'width': '49%'}),html.Div([
html.H1('PS HSUPA Throughput'),
dcc.Graph(
id='graph17')
],style={'background':'#7FDBFF','display': 'inline-block', 'width': '49%'}),
html.Div([
html.H1('PS R99 Setup SR User'),
dcc.Graph(
id='graph18')
],style={'background':'#7FDBFF','display': 'inline-block', 'width': '49%'}),

html.Div([
html.H1('PS R99 Drop Rate User'),
dcc.Graph(
id='graph19')
],style={'background':'#7FDBFF','display': 'inline-block', 'width': '49%'}),
html.Div([
html.H1('PS R99 DL Data Volume'),
dcc.Graph(
id='graph20')
],style={'background':'#7FDBFF','display': 'inline-block', 'width': '49%'}),
html.Div([
html.H1('PS R99 UL Data Volume'),
dcc.Graph(
id='graph21')
],style={'background':'#7FDBFF','display': 'inline-block', 'width': '49%'}),
html.Div([
html.H1('Packet Loss'),
dcc.Graph(
id='graph22')
],style={'background':'#7FDBFF','display': 'inline-block', 'width': '49%'}),html.Div([
html.H1('RRC Drop rate'),
dcc.Graph(
id='graph23')
],style={'background':'#7FDBFF','display': 'inline-block', 'width': '49%'}),

])])
@app.callback(
Output('graph0','figure'), [Input('mydropdown', 'value')])
def upPERIOD_START_TIME_graph0(selected_dropdown_value):
    # loop through each selectd RNC name and add a trace to the graph corresponding to that RNC name
    traces = []
    for RNCname in selected_dropdown_value:
        odf = df[df['RNC name'] == RNCname]
        trace = {'x': odf['PERIOD_START_TIME'], 'y': odf['RRC Connection setup SR'],'name':RNCname}
        traces.append(trace)
    return {'data': traces}
@app.callback(
Output('graph1','figure'), [Input('mydropdown', 'value')])
def upPERIOD_START_TIME_graph1(selected_dropdown_value):
    # loop through each selectd RNC name and add a trace to the graph corresponding to that RNC name
    traces = []
    for RNCname in selected_dropdown_value:
        odf = df[df['RNC name'] == RNCname]
        trace = {'x': odf['PERIOD_START_TIME'], 'y': odf['Call Setup Success Rate CS -Speech'],'name':RNCname}
        traces.append(trace)
    return {'data': traces}
@app.callback(
Output('graph2','figure'), [Input('mydropdown', 'value')])
def upPERIOD_START_TIME_graph2(selected_dropdown_value):
    # loop through each selectd RNC name and add a trace to the graph corresponding to that RNC name
    traces = []
    for RNCname in selected_dropdown_value:
        odf = df[df['RNC name'] == RNCname]
        trace = {'x': odf['PERIOD_START_TIME'], 'y': odf['HSDPA Accessibility'],'name':RNCname}
        traces.append(trace)
    return {'data': traces}
@app.callback(
Output('graph3','figure'), [Input('mydropdown', 'value')])
def upPERIOD_START_TIME_graph3(selected_dropdown_value):
    # loop through each selectd RNC name and add a trace to the graph corresponding to that RNC name
    traces = []
    for RNCname in selected_dropdown_value:
        odf = df[df['RNC name'] == RNCname]
        trace = {'x': odf['PERIOD_START_TIME'], 'y': odf['HSUPA Accessibility'],'name':RNCname}
        traces.append(trace)
    return {'data': traces}
@app.callback(
Output('graph4','figure'), [Input('mydropdown', 'value')])
def upPERIOD_START_TIME_graph4(selected_dropdown_value):
    # loop through each selectd RNC name and add a trace to the graph corresponding to that RNC name
    traces = []
    for RNCname in selected_dropdown_value:
        odf = df[df['RNC name'] == RNCname]
        trace = {'x': odf['PERIOD_START_TIME'], 'y': odf['CSSR for PS'],'name':RNCname}
        traces.append(trace)
    return {'data': traces}
@app.callback(
Output('graph5','figure'), [Input('mydropdown', 'value')])
def upPERIOD_START_TIME_graph5(selected_dropdown_value):
    # loop through each selectd RNC name and add a trace to the graph corresponding to that RNC name
    traces = []
    for RNCname in selected_dropdown_value:
        odf = df[df['RNC name'] == RNCname]
        trace = {'x': odf['PERIOD_START_TIME'], 'y': odf['Soft Handover Success Rate CS and PS'],'name':RNCname}
        traces.append(trace)
    return {'data': traces}
@app.callback(
Output('graph6','figure'), [Input('mydropdown', 'value')])
def upPERIOD_START_TIME_graph6(selected_dropdown_value):
    # loop through each selectd RNC name and add a trace to the graph corresponding to that RNC name
    traces = []
    for RNCname in selected_dropdown_value:
        odf = df[df['RNC name'] == RNCname]
        trace = {'x': odf['PERIOD_START_TIME'], 'y': odf['IRAT HO Success Rate CS'],'name':RNCname}
        traces.append(trace)
    return {'data': traces}	
@app.callback(
Output('graph7','figure'), [Input('mydropdown', 'value')])
def upPERIOD_START_TIME_graph6(selected_dropdown_value):
    # loop through each selectd RNC name and add a trace to the graph corresponding to that RNC name
    traces = []
    for RNCname in selected_dropdown_value:
        odf = df[df['RNC name'] == RNCname]
        trace = {'x': odf['PERIOD_START_TIME'], 'y': odf['3G Traffic CS - Speech'],'name':RNCname}
        traces.append(trace)
    return {'data': traces}
	


@app.callback(
Output('graph8','figure'), [Input('mydropdown', 'value')])
def upPERIOD_START_TIME_graph0(selected_dropdown_value):
    # loop through each selectd RNC name and add a trace to the graph corresponding to that RNC name
    traces = []
    for RNCname in selected_dropdown_value:
        odf = df[df['RNC name'] == RNCname]
        trace = {'x': odf['PERIOD_START_TIME'], 'y': odf['PS HSUPA Volume'],'name':RNCname}
        traces.append(trace)
    return {'data': traces}
@app.callback(
Output('graph9','figure'), [Input('mydropdown', 'value')])
def upPERIOD_START_TIME_graph1(selected_dropdown_value):
    # loop through each selectd RNC name and add a trace to the graph corresponding to that RNC name
    traces = []
    for RNCname in selected_dropdown_value:
        odf = df[df['RNC name'] == RNCname]
        trace = {'x': odf['PERIOD_START_TIME'], 'y': odf['PS HSDPA Volume'],'name':RNCname}
        traces.append(trace)
    return {'data': traces}
@app.callback(
Output('graph10','figure'), [Input('mydropdown', 'value')])
def upPERIOD_START_TIME_graph2(selected_dropdown_value):
    # loop through each selectd RNC name and add a trace to the graph corresponding to that RNC name
    traces = []
    for RNCname in selected_dropdown_value:
        odf = df[df['RNC name'] == RNCname]
        trace = {'x': odf['PERIOD_START_TIME'], 'y': odf['AVG Nbr of HSDPA Users'],'name':RNCname}
        traces.append(trace)
    return {'data': traces}
@app.callback(
Output('graph11','figure'), [Input('mydropdown', 'value')])
def upPERIOD_START_TIME_graph3(selected_dropdown_value):
    # loop through each selectd RNC name and add a trace to the graph corresponding to that RNC name
    traces = []
    for RNCname in selected_dropdown_value:
        odf = df[df['RNC name'] == RNCname]
        trace = {'x': odf['PERIOD_START_TIME'], 'y': odf['AVG Nbr of HSUPA Users'],'name':RNCname}
        traces.append(trace)
    return {'data': traces}
@app.callback(
Output('graph12','figure'), [Input('mydropdown', 'value')])
def upPERIOD_START_TIME_graph4(selected_dropdown_value):
    # loop through each selectd RNC name and add a trace to the graph corresponding to that RNC name
    traces = []
    for RNCname in selected_dropdown_value:
        odf = df[df['RNC name'] == RNCname]
        trace = {'x': odf['PERIOD_START_TIME'], 'y': odf['CS drop rate'],'name':RNCname}
        traces.append(trace)
    return {'data': traces}
@app.callback(
Output('graph13','figure'), [Input('mydropdown', 'value')])
def upPERIOD_START_TIME_graph5(selected_dropdown_value):
    # loop through each selectd RNC name and add a trace to the graph corresponding to that RNC name
    traces = []
    for RNCname in selected_dropdown_value:
        odf = df[df['RNC name'] == RNCname]
        trace = {'x': odf['PERIOD_START_TIME'], 'y': odf['PS Global RAB Drop Rate'],'name':RNCname}
        traces.append(trace)
    return {'data': traces}
@app.callback(
Output('graph14','figure'), [Input('mydropdown', 'value')])
def upPERIOD_START_TIME_graph6(selected_dropdown_value):
    # loop through each selectd RNC name and add a trace to the graph corresponding to that RNC name
    traces = []
    for RNCname in selected_dropdown_value:
        odf = df[df['RNC name'] == RNCname]
        trace = {'x': odf['PERIOD_START_TIME'], 'y': odf['PS HSDPA RAB Drop Rate'],'name':RNCname}
        traces.append(trace)
    return {'data': traces}	
@app.callback(
Output('graph15','figure'), [Input('mydropdown', 'value')])
def upPERIOD_START_TIME_graph6(selected_dropdown_value):
    # loop through each selectd RNC name and add a trace to the graph corresponding to that RNC name
    traces = []
    for RNCname in selected_dropdown_value:
        odf = df[df['RNC name'] == RNCname]
        trace = {'x': odf['PERIOD_START_TIME'], 'y': odf['PS HSUPA RAB Drop Rate'],'name':RNCname}
        traces.append(trace)
    return {'data': traces}
@app.callback(
Output('graph16','figure'), [Input('mydropdown', 'value')])
def upPERIOD_START_TIME_graph0(selected_dropdown_value):
    # loop through each selectd RNC name and add a trace to the graph corresponding to that RNC name
    traces = []
    for RNCname in selected_dropdown_value:
        odf = df[df['RNC name'] == RNCname]
        trace = {'x': odf['PERIOD_START_TIME'], 'y': odf['PS HSDPA Throughput'],'name':RNCname}
        traces.append(trace)
    return {'data': traces}
@app.callback(
Output('graph17','figure'), [Input('mydropdown', 'value')])
def upPERIOD_START_TIME_graph1(selected_dropdown_value):
    # loop through each selectd RNC name and add a trace to the graph corresponding to that RNC name
    traces = []
    for RNCname in selected_dropdown_value:
        odf = df[df['RNC name'] == RNCname]
        trace = {'x': odf['PERIOD_START_TIME'], 'y': odf['PS HSUPA Throughput'],'name':RNCname}
        traces.append(trace)
    return {'data': traces}
@app.callback(
Output('graph18','figure'), [Input('mydropdown', 'value')])
def upPERIOD_START_TIME_graph2(selected_dropdown_value):
    # loop through each selectd RNC name and add a trace to the graph corresponding to that RNC name
    traces = []
    for RNCname in selected_dropdown_value:
        odf = df[df['RNC name'] == RNCname]
        trace = {'x': odf['PERIOD_START_TIME'], 'y': odf['PS R99 Setup SR User'],'name':RNCname}
        traces.append(trace)
    return {'data': traces}
@app.callback(
Output('graph19','figure'), [Input('mydropdown', 'value')])
def upPERIOD_START_TIME_graph3(selected_dropdown_value):
    # loop through each selectd RNC name and add a trace to the graph corresponding to that RNC name
    traces = []
    for RNCname in selected_dropdown_value:
        odf = df[df['RNC name'] == RNCname]
        trace = {'x': odf['PERIOD_START_TIME'], 'y': odf['PS R99 Drop Rate User'],'name':RNCname}
        traces.append(trace)
    return {'data': traces}
@app.callback(
Output('graph20','figure'), [Input('mydropdown', 'value')])
def upPERIOD_START_TIME_graph4(selected_dropdown_value):
    # loop through each selectd RNC name and add a trace to the graph corresponding to that RNC name
    traces = []
    for RNCname in selected_dropdown_value:
        odf = df[df['RNC name'] == RNCname]
        trace = {'x': odf['PERIOD_START_TIME'], 'y': odf['PS R99 DL Data Volume'],'name':RNCname}
        traces.append(trace)
    return {'data': traces}
@app.callback(
Output('graph21','figure'), [Input('mydropdown', 'value')])
def upPERIOD_START_TIME_graph5(selected_dropdown_value):
    # loop through each selectd RNC name and add a trace to the graph corresponding to that RNC name
    traces = []
    for RNCname in selected_dropdown_value:
        odf = df[df['RNC name'] == RNCname]
        trace = {'x': odf['PERIOD_START_TIME'], 'y': odf['PS R99 UL Data Volume'],'name':RNCname}
        traces.append(trace)
    return {'data': traces}
@app.callback(
Output('graph22','figure'), [Input('mydropdown', 'value')])
def upPERIOD_START_TIME_graph6(selected_dropdown_value):
    # loop through each selectd RNC name and add a trace to the graph corresponding to that RNC name
    traces = []
    for RNCname in selected_dropdown_value:
        odf = df[df['RNC name'] == RNCname]
        trace = {'x': odf['PERIOD_START_TIME'], 'y': odf['Packet Loss'],'name':RNCname}
        traces.append(trace)
    return {'data': traces}	
@app.callback(
Output('graph23','figure'), [Input('mydropdown', 'value')])
def upPERIOD_START_TIME_graph6(selected_dropdown_value):
    # loop through each selectd RNC name and add a trace to the graph corresponding to that RNC name
    traces = []
    for RNCname in selected_dropdown_value:
        odf = df[df['RNC name'] == RNCname]
        trace = {'x': odf['PERIOD_START_TIME'], 'y': odf['RRC Drop rate'],'name':RNCname}
        traces.append(trace)
    return {'data': traces}
@app.callback(
Output('graph24','figure'), [Input('mydropdown', 'value')])
def upPERIOD_START_TIME_graph0(selected_dropdown_value):
    # loop through each selectd RNC name and add a trace to the graph corresponding to that RNC name
    traces = []
    for RNCname in selected_dropdown_value:
        odf = df[df['RNC name'] == RNCname]
        trace = {'x': odf['PERIOD_START_TIME'], 'y': odf['RRC Connection setup SR'],'name':RNCname}
        traces.append(trace)
    return {'data': traces}
@app.callback(
Output('graph25','figure'), [Input('mydropdown', 'value')])
def upPERIOD_START_TIME_graph1(selected_dropdown_value):
    # loop through each selectd RNC name and add a trace to the graph corresponding to that RNC name
    traces = []
    for RNCname in selected_dropdown_value:
        odf = df[df['RNC name'] == RNCname]
        trace = {'x': odf['PERIOD_START_TIME'], 'y': odf['Call Setup Success Rate CS -Speech'],'name':RNCname}
        traces.append(trace)
    return {'data': traces}

if __name__ == '__main__':
    app.run_server(debug=True)
