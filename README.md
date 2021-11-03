# GoldenGate Examples using Ansible


These scripts let you create and update your OCI GoldenGate Instance:

* OCI_GG_Create_Deployment.yml
* OCI_GG_REGISTER_DATABASE.yml
* OCI_GG_UPDATE_DEPLOYMENT.yml

Check this [link](https://oci-ansible-collection.readthedocs.io/en/latest/collections/oracle/oci/oci_golden_gate_deployment_module.html#ansible-collections-oracle-oci-oci-golden-gate-deployment-module) to get more information about the different Ansible modules to OCI GoldenGate.

---

### GoldenGate REST APIs

We can take advantage of GoldenGate REST APIs and use them in Ansible. You can create extracts, replicats, parameter file and so on with REST APIs. Here you have a couple of examples:

* OCI_GG_CREATE_EXTRACT.yml
* OCI_GG_CREATE_REPLICAT.yml 
* OCI_GG_DELETE_EXTRACT.yml
* OCI_GG_DELETE_REPLICAT.yml
* OCI_GG_RESET_DEVELOPMENT.yml

Check all GoldenGate REST APIs on [documentation](https://docs.oracle.com/en/middleware/goldengate/core/21.3/oggra/rest-endpoints.html).
