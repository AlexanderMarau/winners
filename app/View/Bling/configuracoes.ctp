<form action="/bling/salvar" method="POST">
	<div id="page-wrapper">
	    <div class="row">
	        <div class="col-lg-12">
	            <h1 class="page-header">Bling</h1>
	        </div>
	        <!-- /.col-lg-12 -->
	    </div>
	    <!-- /.row -->
	    <div class="row">

	    	<div class="col-lg-12">

				<!-- Nav tabs -->
				<ul class="nav nav-tabs" role="tablist">
					<li role="presentation" class="active">
						<a href="#chaves" aria-controls="chaves" role="tab" data-toggle="tab">Chaves</a>
					</li>
					<li role="presentation">
						<a href="#vendas" aria-controls="vendas" role="tab" data-toggle="tab">Vendas</a>
					</li>
				</ul>

				<!-- Tab panes -->
				<div class="tab-content">
					
					<div role="tabpanel" class="tab-pane active" id="chaves">
						<div class="row" style="margin-top:30px;">
			                 <div class="col-md-12">
			                    <div class="form-group">
			                        <label>Chave de API</label>
			                        <input class="form-control" name="dados[api_key]" value="<?php echo isset($dados['Bling']['api_key']) ? $dados['Bling']['api_key'] : ''; ?>">
			                    </div>
			                 </div>
		                </div>
					</div>

					<div role="tabpanel" class="tab-pane" id="vendas">
						<div class="row" style="margin-top:30px;">
			                 <div class="col-md-12">

				                <div class="panel-body">
				                    <div class="table-responsive">
				                        <table class="table table-striped table-bordered table-hover" id="dataTables-pedidosBlings">
				                            <thead>
				                                <tr>
				                                    <th>ID</th>
				                                    <th>ID Winners</th>
				                                    <th>ID Bling</th>
				                                    <th>Valor</th>
				                                    <th>Ações</th>
				                                </tr>
				                            </thead>
				                            <tbody>   

				                            </tbody>
				                        </table>
				                    </div>
				                    <!-- /.table-responsive -->
				                </div>

			                 </div>
		                </div>
					</div>

				</div>

			</div>


	    </div>

	    <div class="row text-right">
	    	<div class="col-lg-12">
				<button class="text-right btn btn-success">Salvar</button>
			</div>
		</div>

	</div>
</form>