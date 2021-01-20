Title: Terraform: Getting Started
Date: 2021-1-17 21:32
Modified: 2021-1-17 21:32
Category:
Tags: Terraform, IAC, Terraform Cloud
Slug: straight-up-Terraform
Summary: This is the very detailed introduction to getting started with Terraform

> Terraform is an open-source infrastructure as code software tool that enables you to safely and predictably create, change, and improve infrastructure. - www.Terraform.io

<!--toc-->

- [Chapter 1: Introduction to IaC](#chapter-1-introduction-to-iac)
        * [1.1 Begin with a look back](#11-begin-with-a-look-back)
        * [1.2 Why infrastructure as code?](#12-why-infrastructure-as-code)
        * [1.3 Terminology](#13-terminology)
        * [1.4 Explore approaches to IaC](#14-explore-approaches-to-iac)
- [Chapter 2: Terraform](#chapter-2-terraform)
        * [2.1 What is Terraform?](#21-what-is-terraform)
        * [2.2 Install Terraform](#22-install-terraform)
        * [2.3 Terraform Tour](#23-terraform-tour)
        * [2.4 The very "Basics of Terraform"](#24-the-very-basics-of-terraform)
- [Chapter 3: Learning HCL](#chapter-3-learning-hcl)
        * [3.1 Overview of HCL structure](#31-overview-of-hcl-structure)
        * [3.2 Terraform data sources and resources](#32-terraform-data-sources-and-resources)
        * [3.3 Terraform Outputs](#33-terraform-outputs)
        * [3.4 Interpolation in HCL](#34-interpolation-in-hcl)
        * [3.5 Dependencies in Terraform](#35-dependencies-in-terraform)
        * [3.6 Variables and Locals](#36-variables-and-locals)
        * [3.7 Conditionals and the Count property](#37-conditionals-and-the-count-property)
        * [3.8 Data types and operators](#38-data-types-and-operators)
        * [3.9 Functions](#39-functions)
        * [3.10 Iterations in collections](#310-iterations-in-collections)
        * [3.11 Directives and heredocs](#311-directives-and-heredocs)
        * [3.12 Clean up](#312-clean-up)
- [Chapter 4: Code Re-Use for applying DRY](#chapter-4-code-re-use-for-applying-dry)
        * [4.1 Understanding Terraform Modules](#41-understanding-terraform-modules)
        * [4.2 Distributing modules](#42-distributing-modules)
- [Chapter 5: Collaboration with Terraform](#chapter-5-collaboration-with-terraform)
        * [5.1 Terraform backends](#51-terraform-backends)
        * [5.2 Terraform workspaces](#52-terraform-workspaces)

# Chapter 1: Introduction to IaC

### 1.1 Begin with a look back

- [1960-1970] - Mainframe Computers
    - Big machines
    - Big facilities and using fork-lifts to move machines
    - Automation was not that critical in this era
- [1980-1990] - Client/Server World
    - Things started to get little more complicated
    - UNIX or PC servers running various OS
    - These machines serve users using networking
- [Mid 90's-2000] - Virtualization
    - Software defines infrastructures
    - Hardware were virtualized
    - Clients do not have any hardware debt
- Cloud Era
    - No hardware to manage
    - It's all software management problem
    - All these things could be managed by API's, Scripts
    - Manage all the infrastructures by the code


### 1.2 Why infrastructure as code?

- Repeatability
    - We can deploy the same thing over and over again
    - We'll have a backup
    - We can have multiple environments (dev, stage, prod)
- Auditability
    - We can see what changed, who changed and impact of change
    - We can detect the problems easily
- Change control
    - Allows us to use VCS to control what to change
- Collaboration
    - Multiple people can work together on the same code base
    - Example: Use GitHub to propose a change

### 1.3 Terminology

- **IaC** - Infrastructure as Code
- **CM** - Configuration Management (Example: Ansible, Puppet, etc)
- **IaaS** - Infrastructure as a Service (Example: AWS, GoogleCloud, Azure)
- **PaaS** - Platform as a Service (Example: Heroku, AWS EBS)
- **VCS** - Version Control System
- **CI/CD** - Continuous Integration/ Continuous Deployment (Delivery)
- **SDLC** - Software Development Life Cycle
- **Declarative** - Declare what you want
- **Imperative** - How to get the desired state

### 1.4 Explore approaches to IaC

- Imperative Approach
    - Procedural Approach
    - Answers How?
    - Example Tools: AWS Cli, Python/Boto3
- Declarative Approach
    - Answers What?
    - Example Tools: AWS CloudFormation, Terraform
    - We can change things easily for example AWS instance type
    - Tool does everything for us


# Chapter 2: Terraform

### 2.1 What is Terraform?

- Terraform is a cross-platform command line tool
- Declarative IaC tool
    - We define what we want and Terraform will create it for us
- Also, an Online Service
    - Provided through Terraform Cloud
    - Remote execution, Secret Storage
- Terraform consists
    - **Configuration**: Configuration files to define what we want
    - **State**: Like a Database which stores the current state and can be stored anywhere like in local PC, S3, GCS, Google Drive, etc
        - State is the Terraform view of the world
        - Terraform looks here instead of cloud provider
        - Terraform compares **Config and State** to create-destroy resource

### 2.2 Install Terraform

[https://www.Terraform.io/downloads.html](https://www.Terraform.io/downloads.html)

```shell
╰─$ terraform -version
Terraform v0.14.4
```

### 2.3 Terraform Tour

Initialize Terraform

```shell
╭─sagar-giri@PCN-489 ~/IdeaProjects/HelloTerraform
╰─$ terraform init
Terraform initialized in an empty directory!

The directory has no Terraform configuration files. You may begin working
with Terraform immediately by creating Terraform configuration files.
```

Plan Terraform

```shell
╭─sagar-giri@PCN-489 ~/IdeaProjects/HelloTerraform
╰─$ terraform plan

Error: No configuration files

Plan requires configuration to be present. Planning without a configuration
would mark everything for destruction, which is normally not what is desired.
If you would like to destroy everything, run plan with the -destroy option.
Otherwise, create a Terraform configuration file (.tf file) and try again.
```

Apply

```shell
╭─sagar-giri@PCN-489 ~/IdeaProjects/HelloTerraform
╰─$ terraform apply                                                                                                 1 ↵

Error: No configuration files

Apply requires configuration to be present. Applying without a configuration
would mark everything for destruction, which is normally not what is desired.
If you would like to destroy everything, run 'Terraform destroy' instead.
```

Destroy

```shell
╭─sagar-giri@PCN-489 ~/IdeaProjects/HelloTerraform
╰─$ terraform destroy
Do you really want to destroy all resources?
  Terraform will destroy all your managed infrastructure, as shown above.
  There is no undo. Only 'yes' will be accepted to confirm.

  Enter a value: no

Destroy cancelled.
╭─sagar-giri@PCN-489 ~/IdeaProjects/HelloTerraform
╰─$ terraform destroy                                                                                               1 ↵
Do you really want to destroy all resources?
  Terraform will destroy all your managed infrastructure, as shown above.
  There is no undo. Only 'yes' will be accepted to confirm.

  Enter a value: yes

Destroy complete! Resources: 0 destroyed.
```

Help (Look for the _**Main commands**_ section)

```shell
╰─$ terraform help
Usage: Terraform [global options] <subcommand> [args]

The available commands for execution are listed below.
The primary workflow commands are given first, followed by
less common or more advanced commands.

Main commands:
  init          Prepare your working directory for other commands
  validate      Check whether the configuration is valid
  plan          Show changes required by the current configuration
  apply         Create or update infrastructure
  destroy       Destroy previously-created infrastructure

All other commands:
  console       Try Terraform expressions at an interactive command prompt
  fmt           Reformat your configuration in the standard style
  force-unlock  Release a stuck lock on the current workspace
  get           Install or upgrade remote Terraform modules
  graph         Generate a Graphviz graph of the steps in an operation
  import        Associate existing infrastructure with a Terraform resource
  login         Obtain and save credentials for a remote host
  logout        Remove locally-stored credentials for a remote host
  output        Show output values from your root module
  providers     Show the providers required for this configuration
  refresh       Update the state to match remote systems
  show          Show the current state or a saved plan
  state         Advanced state management
  taint         Mark a resource instance as not fully functional
  untaint       Remove the 'tainted' state from a resource instance
  version       Show the current Terraform version
  workspace     Workspace management

Global options (use these before the subcommand, if any):
  -chdir=DIR    Switch to a different working directory before executing the
                given subcommand.
  -help         Show this help output, or the help for a specified subcommand.
  -version      An alias for the "version" subcommand.
```
Format the Terraform file

```shell
╰─$ terraform fmt
```

### 2.4 The very "Basics of Terraform"

Terraform uses HCL ([HashiCorp](https://github.com/hashicorp) Configuration Language)

The extension of file ends with `.tf`

Create `main.tf` inside a directory

```none
"greeting" {
   value = "Hello Terraform."
 }

 provider "random" {}
```

Initialize Terraform

```shell
╰─$ terraform init

Initializing the backend...

Initializing provider plugins...
- Finding latest version of hashicorp/random...
- Installing hashicorp/random v3.0.1...
- Installed hashicorp/random v3.0.1 (signed by HashiCorp)

Terraform has created a lock file .Terraform.lock.hcl to record the provider
selections it made above. Include this file in your version control repository
so that Terraform can guarantee to make the same selections by default when
you run "Terraform init" in the future.

Terraform has been successfully initialized!

You may now begin working with Terraform. Try running "terraform plan" to see
any changes that are required for your infrastructure. All Terraform commands
should now work.

If you ever set or change modules or backend configuration for Terraform,
rerun this command to reinitialize your working directory. If you forget, other
commands will detect it and remind you to do so if necessary.
```

Plan it

```shell
╰─$ terraform plan

An execution plan has been generated and is shown below.
Resource actions are indicated with the following symbols:

Terraform will perform the following actions:

Plan: 0 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + greeting = "Hello Terraform."

------------------------------------------------------------------------

Note: You didn't specify an "-out" parameter to save this plan, so Terraform
can't guarantee that exactly these actions will be performed if
"Terraform apply" is subsequently run.

```

Apply it. You might have to type `yes` in the middle of it.

After applying it creates a `.tfstate` file, and you should not touch the `.tfstate` file.

```shell
╰─$ terraform apply

An execution plan has been generated and is shown below.
Resource actions are indicated with the following symbols:

Terraform will perform the following actions:

Plan: 0 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + greeting = "Hello Terraform."

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes


Apply complete! Resources: 0 added, 0 changed, 0 destroyed.

Outputs:

greeting = "Hello Terraform."
```

See the output

```shell
╰─$ terraform output
greeting = "Hello Terraform."
```

Specify which output you want

```shell
╰─$ terraform output greeting
"Hello Terraform."
```

# Chapter 3: Learning HCL

### 3.1 Overview of HCL structure

By conventions `main.tf` , `outputs.tf` and `variables.tf` are required files inside a directory

Sometimes the `main.tf` file gets too big. In this case we use the submodules.

Example `main.tf` with AWS as a provider:

```hcl
# Terraform block is optional but it's a best practice to have it
terraform {
  # required_version is the Terraform version which we want to apply
  required_version = ">=0.14.0"
}

# Which cloud provider you want to use
provider "aws" {
  # region is required
  region = "ap-northeast-1"

  # Since I am putting this file in GitHub I do not EVER put my AWS credentials here.
  # Instead I use the environment variable or Terraform cloud or the ~/.aws/credentials file
  #access_keys = "my-access-key"
  #access_secret = "my-secret-key"
}

```

### 3.2 Terraform data sources and resources

- Resources
    - Resource is any object that you want to manage with Terraform. For example: S3, AWS EKS, GKE, VM's.
    - Resources are defined in the resource block
    - Declaring a resource tells Terraform that it should CREATE and manage the Resource described.
    - If the resource already exists, it must be imported into Terraform state.
    - Example: `resource "aws_s3_bucket" "Terraform-bucket-2021" {}`
    - REF: [https://www.Terraform.io/docs/configuration/blocks/resources/index.html](https://www.Terraform.io/docs/configuration/blocks/resources/index.html)
- Data sources
    - Data sources are resources that Terraform does not manage. For example: _Availability Zones, Account ID_
    - We can use data source to get the availability zones to place EC2 instances in multiple AZ's
    - REF: [https://www.Terraform.io/docs/configuration/data-sources.html](https://www.Terraform.io/docs/configuration/data-sources.html)
Example:

**Create a S3 bucket in AWS using resource block.**

```hcl
terraform {
  required_version = ">=0.14.0"
}

provider "aws" {
  region = "ap-northeast-1"
}

resource "aws_s3_bucket" "Terraform-bucket-2021" {
  # bucket name should be unique.
  # If you don't provide any name, Terraform will create it for you and saves in outputs.tf file
  bucket = "Terraform-bucket-2021"
}
```

Plan and save the output to a file using command: `terraform plan -out s3.tfplan` . This will create a file named `s3.tfplan` with following output:

```bash
╰─$ terraform plan -out example.tfplan

An execution plan has been generated and is shown below.
Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # aws_s3_bucket.Terraform-bucket-2021 will be created
  + resource "aws_s3_bucket" "Terraform-bucket-2021" {
      + acceleration_status         = (known after apply)
      + acl                         = "private"
      + arn                         = (known after apply)
      + bucket                      = "Terraform-bucket-2021"
      + bucket_domain_name          = (known after apply)
      + bucket_regional_domain_name = (known after apply)
      + force_destroy               = false
      + hosted_zone_id              = (known after apply)
      + id                          = (known after apply)
      + region                      = (known after apply)
      + request_payer               = (known after apply)
      + website_domain              = (known after apply)
      + website_endpoint            = (known after apply)

      + versioning {
          + enabled    = (known after apply)
          + mfa_delete = (known after apply)
        }
    }

Plan: 1 to add, 0 to change, 0 to destroy.

------------------------------------------------------------------------

This plan was saved to: example.tfplan

To perform exactly these actions, run the following command to apply:
    Terraform apply "example.tfplan"
```

Anything beginning with the `+` means Terraform will create this resource for us. In the output above, it's `+ create` which means the resource doesn't exist yet and Terraform will perform `create` operation on the resource.

Now, apply the plan using command: `terraform apply s3.tfplan`

Once applied, following output will be seen:

```none
╰─$ terraform apply example.tfplan
aws_s3_bucket.Terraform-bucket-2021: Creating...
aws_s3_bucket.Terraform-bucket-2021: Creation complete after 5s [id=Terraform-bucket-2021]

Apply complete! Resources: 1 added, 0 changed, 0 destroyed.

The state of your infrastructure has been saved to the path
below. This state is required to modify and destroy your
infrastructure, so keep it safe. To inspect the complete state
use the `terraform show` command.

State path: Terraform.tfstate

```

It means that the s3 bucket has been created.

Verify if the bucket exist using `aws s3 ls` command

```shell
╰─$ aws s3 ls
2021-01-16 19:42:52 Terraform-bucket-2021
```
Bucket is successfully created 🎉

> _Note: In real world, you ought to share the plan with your colleagues and there's an agreement between collegues before applying it._

### 3.3 Terraform Outputs

When we don't define some value (bucket name for example), Terraform will create the bucket name for us, and we can know the bucket details using Terraform outputs.

In above case, let's output the bucket information of `terraform-bucket-2021`

To do that we need to create a output block

```hcl
resource "aws_s3_bucket" "Terraform-bucket-2021" {
  bucket = "Terraform-bucket-2021"
}

output "bucket_info" {
  # <syntax> value = resource_type[.]label_name
  value = aws_s3_bucket.Terraform-bucket-2021
}
```

Now, plan it `terraform plan -out s3.tfplan` . Here, the previous filename `s3.tfplan` will be replaced with the new fresh file.

Not apply the `s3.tfplan` using command `terraform apply s3.tfplan`

You'll see following output:

```bash
Apply complete! Resources: 0 added, 0 changed, 0 destroyed.

Outputs:

bucket_info = {
  "acceleration_status" = ""
  "acl" = "private"
  "arn" = "arn:aws:s3:::Terraform-bucket-2021"
  "bucket" = "Terraform-bucket-2021"
  "bucket_domain_name" = "Terraform-bucket-2021.s3.amazonaws.com"
  "bucket_prefix" = tostring(null)
  "bucket_regional_domain_name" = "Terraform-bucket-2021.s3.ap-northeast-1.amazonaws.com"
  "cors_rule" = tolist([])
  "force_destroy" = false
  "grant" = toset([])
  "hosted_zone_id" = "Z2M4EHUR26P7ZW"
  "id" = "Terraform-bucket-2021"
  "lifecycle_rule" = tolist([])
  "logging" = toset([])
  "object_lock_configuration" = tolist([])
  "policy" = tostring(null)
  "region" = "ap-northeast-1"
  "replication_configuration" = tolist([])
  "request_payer" = "BucketOwner"
  "server_side_encryption_configuration" = tolist([])
  "tags" = tomap({})
  "versioning" = tolist([
    {
      "enabled" = false
      "mfa_delete" = false
    },
  ])
  "website" = tolist([])
  "website_domain" = tostring(null)
  "website_endpoint" = tostring(null)
}
```

As you can see `Apply complete! Resources: 0 added, 0 changed, 0 destroyed.` because no resources were created even though our `.tf` file has resource block.

You can also get the output using `terraform output` command like this: `terraform output bucket_info`

Example:

**List output of availability zones of region configured in your AWS configuration**

First, create the data block because regions are not managed by Terraform and it's a data. And the output block. Since the output is from the data block, we define value as: `data.<type>.<label>`

```hcl
data "aws_availability_zones" "available" {
  state = "available"
}

output "aws_availability_zones" {
  value = data.aws_availability_zones.available
}
```

Now, plan it `terraform plan -out s3.tfplan`  and apply `terraform apply s3.tfplan`

You'll see following output:

```bash
Apply complete! Resources: 0 added, 0 changed, 0 destroyed.

Outputs:

aws_availability_zones = {
  "all_availability_zones" = tobool(null)
  "blacklisted_names" = toset(null) /* of string */
  "blacklisted_zone_ids" = toset(null) /* of string */
  "exclude_names" = toset(null) /* of string */
  "exclude_zone_ids" = toset(null) /* of string */
  "filter" = toset(null) /* of object */
  "group_names" = toset([
    "ap-northeast-1",
  ])
  "id" = "2021-01-16 10:53:54.916848 +0000 UTC"
  "names" = tolist([
    "ap-northeast-1a",
    "ap-northeast-1c",
    "ap-northeast-1d",
  ])
  "state" = "available"
  "zone_ids" = tolist([
    "apne1-az4",
    "apne1-az1",
    "apne1-az2",
  ])
}

```
> Note: The output of AZ's can be used later on if we want to provision EC2 instances in multiple regions. We can use this output to do it so.

### 3.4 Interpolation in HCL

Interpolation is just the means of concatenating different values to create one value. In case of S3 bucket the value of S3 bucket has to be globally unique. Hence, inorder to create a bucket with unique name, we can use interpolation.

Example:

**Create aws bucket which name has the ****`accountID`**** in it.**

```hcl
data "aws_caller_identity" "current" {}

resource "aws_s3_bucket" "bucket2" {
  bucket = "${data.aws_caller_identity.current.account_id}-bucket2"
}

```
Here `data.aws_caller_identity.current.account_id` is interpolated which is `account_id + "-bucket2"` got from the data block `aws_caller_identity`

### 3.5 Dependencies in Terraform

Terraform has the concept of `implicit` and `explicit` dependencies.

Whe Terraform processes the HCL configs, it evaluates the dependency graph, and it'll create dependencies before it creates the dependent resource. If there is not any dependencies, Terraform will create resource in parallel which will give performance boost.

Example:

Implicit dependency resolve when the dependent resource already exists.

```hcl
resource "aws_s3_bucket" "bucket3" {
  bucket = "${data.aws_caller_identity.current.account_id}-bucket3"
  tags = {
    # I already have bucket2 available so this is implicit
    dependency = aws_s3_bucket.bucket2.arn
  }
}
```
Explicit dependency when the dependent resource does not exist yet, and we need to wait for it to be created first. (analogy depends

```hcl
resource "aws_s3_bucket" "bucket4" {
  bucket = "${data.aws_caller_identity.current.account_id}-bucket4"
  # Explicit
  depends_on = [
    aws_s3_bucket.bucket3
  ]
}
```
To see the dependencies, generate the `dot` file using `terraform graph > graph.dot`

And paste the content in online tool [https://dreampuf.github.io/GraphvizOnline/](https://dreampuf.github.io/GraphvizOnline/) to see the output.

The `terraform graph` command is only used for debugging purpose.

### 3.6 Variables and Locals

Variables are ways to get input to the Terraform config

Ways to provide variables:

- Using command line while applying
- Specify them in files such as `.tfvars` or `.auto.tfvars` for complex data types
- Using environment variables but all the environment variable name should have prefix of `TF_VAR_`
In Terraform config, we use `variable` block to define expected variables.

Example:

**Create a S3 bucket, but the bucket name should be provided by the user**

```hcl
variable "bucket_name" {
  type = string

  # `default` is optional. If default is omitted, then value must be supplied
  # default = "My_Bucket1234"
}

resource "aws_s3_bucket" "bucket5" {
  bucket = var.bucket_name
}
```
And when plan is executed, the bucket name is expected as an input value:

```bash
$ terraform plan -out var.tfplan
var.bucket_name
  Enter a value: MyPiBucket31415

An execution plan has been generated and is shown below.
Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # aws_s3_bucket.bucket5 will be created
  + resource "aws_s3_bucket" "bucket5" {
      + acceleration_status         = (known after apply)
      + acl                         = "private"
      + arn                         = (known after apply)
      + bucket                      = "MyPiBucket31415"
      + bucket_domain_name          = (known after apply)
      + bucket_regional_domain_name = (known after apply)
      + force_destroy               = false
      + hosted_zone_id              = (known after apply)
      + id                          = (known after apply)
      + region                      = (known after apply)
      + request_payer               = (known after apply)
      + website_domain              = (known after apply)
      + website_endpoint            = (known after apply)

      + versioning {
          + enabled    = (known after apply)
          + mfa_delete = (known after apply)
        }
    }

Plan: 1 to add, 0 to change, 0 to destroy.

```
**Local values**

Local values make Terraform configs more readable.

If we want to use same value multiple times in the code, it's better to save it as a local value.

We can have multiple locals, but the names should be unique because names are global.

Example:

```hcl
locals {
  aws_account = "${data.aws_caller_identity.current.account_id}-${lower(data.aws_caller_identity.current.user_id)}"
}

resource "aws_s3_bucket" "bucket6" {
  bucket = "${local.aws_account}-bucket6"
}
```
> Note: Here the
> `lower()`
>  is a Terraform function. See more here:
> [https://www.Terraform.io/docs/configuration/functions.html](https://www.Terraform.io/docs/configuration/functions.html)

### 3.7 Conditionals and the Count property

Count is the meta attribute of Terraform

Count means instead of creating 1 resource, you can define `n` number of count to replicate the same resource.

Example:

**Create 2 buckets**

```hcl
resource "aws_s3_bucket" "bucketX" {
  count = 2
  bucket = "${local.aws_account}-bucket${count.index+7}"
}
```

Q. What happens when `count=0` ?

Terraform will destroy all resource if created or not create anything if it's not created yet.

**We can also replicate resources using ****`for_each`****  **

```hcl
locals {
  buckets = {
    bucket101 = "mybucket101"
    bucket102 = "mybucket102"
  }
}

resource "aws_s3_bucket" "bucketIterator" {
  for_each = local.buckets
  bucket = "${local.aws_account}-${each.value}"
}

output "bucketIterator" {
  value = aws_s3_bucket.bucketIterator
}
```
We can also define list instead of map:

```hcl
locals {
  buckets = [
  "mybucket101",
  "mybucket102"
  ]
}

resource "aws_s3_bucket" "bucketIterator" {
  # Since buckets is a list, we need to convert to set using toset()
  for_each = toset(local.buckets)
  # Here we can use either .key or .value
  bucket = "${local.aws_account}-${each.key}"
}

output "bucketIterator" {
  value = aws_s3_bucket.bucketIterator
}
```
`count` vs `for_each`


- `count` is generally used for toggle switch when in development phase

- `for_each` is more powerful, as we can use map in `for_each` hence, better to use `for_each` in prod
### 3.8 Data types and operators

REF: [https://www.Terraform.io/docs/configuration/expressions/types.html](https://www.Terraform.io/docs/configuration/expressions/types.html)

```hcl
locals {
  a_string = "This is a String"
  a_number = 3.1415
  a_boolean = true
  a_list = [
    "element1",
    true,
    [1, 2, 3]
  ]
  a_map = {
    key = "value"
    nums = [10, 20, 30]
    is_active = true
    configs = {
      instance_type = "t2.micro"
      vpc_enabled  = true
    }
  }

  # Operators
  operators = (3+3)-(3*3/3)

  # Logical
  t = true && true
  f = true || false

  # Comparison
  gt = 3 > 2
  lt = 4 < 9
  eq = 4 == 4
  neq = 4 != 5
}
```

Example:

**Terraform config to create ****`n`**** number of buckets where ****`n`**** not more than ****`5`**** **

```hcl
variable "bucket_count" {
  type = number
}

data "aws_caller_identity" "current" {}

locals {
  min_bucket_count = 5
  # Conditional operators similar to ternary operator
  num_buckets = var.bucket_count > 5 ? local.min_bucket_count: var.bucket_count
  aws_account = "${data.aws_caller_identity.current.account_id}-${lower(data.aws_caller_identity.current.user_id)}"
}

resource "aws_s3_bucket" "buckets" {
  count = local.num_buckets
  bucket = "${local.aws_account}-buckets${count.index+7}"
}
```

### 3.9 Functions

REF: [https[://www.Terraform.io/docs/configuration/functions.html](https://www.Terraform.io/docs/configuration/functions.html)](https://www.Terraform.io/docs/configuration/functions.html)

Example:

```hcl
locals {
  ts = timestamp()
  current_month = formatdate("MMMM", local.ts)
  tomorrow = formatdate("MMMM", timeadd(local.ts, "24h"))
  upper = upper("lowercase")
  lower = lower("UPPERCASE")
}

output "func" {
  value = "${local.ts} ${local.current_month} ${local.tomorrow} ${local.upper} ${local.lower}"
}
```

Output:

```bash
Apply complete! Resources: 0 added, 0 changed, 0 destroyed.

Outputs:

func = "2021-01-16T15:36:41Z January January LOWERCASE uppercase"
```
### 3.10 Iterations in collections

HCL uses `for` syntax dfor iterating over list values

Example:

```hcl
locals {
  my_list    = ["one", "two", "three"]
  upper_list = [for item in local.my_list : upper(item)]
  upper_map  = { for item in local.my_list : item => upper(item) }

  # Filtering
  n     = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  evens = [for i in local.n : i if i % 2 == 0]
}

output "my_list" {
  value = local.my_list
}
output "upper_list" {
  value = local.upper_list
}

output "upper_map" {
  value = local.upper_map
}

output "evens" {
  value = local.evens
}
```
Output after apply:

```shell

Apply complete! Resources: 0 added, 0 changed, 0 destroyed.

Outputs:

evens = [
  2,
  4,
  6,
  8,
]
my_list = [
  "one",
  "two",
  "three",
]
upper_list = [
  "ONE",
  "TWO",
  "THREE",
]
upper_map = {
  "one" = "ONE"
  "three" = "THREE"
  "two" = "TWO"
}
```
### 3.11 Directives and heredocs


- `heredocs`
    - is a multiline string that is used to create an inline JSON documents
    - They are used in outputs, variables description and inline documents
Example:

```hcl
locals {
  count = 0
  nums  = [1, 2, 3]
}
output "heredocs" {
  # EOT means EOF
  value = <<-EOT
    This is the `heredoc`.
    This is multiline String.
    Used for writing documentations.
  EOT
  # Dont forget EOT at the end
}

output "directive" {
  value = <<-EOT
    We can use directive in heredoc.
    %{if local.count == 0}
    The count is 0, destroying everything...
    %{else}
    The count is ${local.count}
    %{endif}
  EOT
}

output "iterated-directive" {
  value = <<-EOT
    Directive can also be iterated.
    %{for num in local.nums}
    ${num}
    %{endfor}
  EOT
}
```

Output after apply:

```bash
Apply complete! Resources: 0 added, 0 changed, 0 destroyed.

Outputs:

directive = <<EOT
We can use directive in heredoc.

The count is 0, destroying everything...


EOT
heredocs = <<EOT
This is the `heredoc`.
This is multiline String.
Used for writing documentations.

EOT
iterated-directive = <<EOT
Directive can also be iterated.

1

2

3


EOT

```

### 3.12 Clean up

Since we created multiple buckets and all, it's time to clean up.

Even though the buckets don't cost any, it's wise to clean up since we're just playing with Terraform in development mode.

First look for states that's tracked by Terraform using `terraform state list` . If it shows bunch of outputs of your bucket, execute `terraform destroy` which will destroy all resources that were created.

# Chapter 4: Code Re-Use for applying DRY

### 4.1 Understanding Terraform Modules

What is a module in Terraform?


- All Terraform is in a module. The top level module is called the Root module
- Modules are just a directory that contains Terraform file, and they can be nested
- Modules can be imported which are already available
- Modules written by others can be get here [https://registry.Terraform.io](https://registry.Terraform.io)
- Module helps in implementing DRY principle
- Module naming convention (if you want to publish to Terraform registry)
    - `terraform-<PROVIDER>-<NAME>`
    - `<NAME>` can contain hyphens
Module layout

```bash
├── Terraform-aws-s3
│   ├── README.md
│   ├── datas.tf
│   ├── locals.tf
│   ├── main.tf
│   ├── outputs.tf
│   ├── variables.tf
│   └── versions.tf

```
You can use [https://github.com/QuiNovas/cookiecutter-Terraform-module](https://github.com/QuiNovas/cookiecutter-Terraform-module) to automate the process of creating these files

To use module

```none
# Module located in local filesystem
module "local-module" {
    source = "/path/to/module"
}

# Module which is published
module "published-module" {
    source = "rojopolis/Terraform-aws-lambda-python-archive"
    version = "1.2.3"
}

# Module which is in GitHub
module "github-module" {
    source = "https://github.com/rojopolis/Terraform-aws-lambda-python-archive"
}
```
Play with [https://github.com/rojopolis/Terraform-aws-lambda-python-archive/](https://github.com/rojopolis/Terraform-aws-lambda-python-archive/) to know about modules.

### 4.2 Distributing modules


- Name the module properly `terraform-<PROVIDER>-<NAME>`
- Should be in public repository in GitHub.
- Should have license and examples
- Repo should be released with a tag
- Sign-in to [https://registry.Terraform.io](https://registry.Terraform.io)
- Select the repo which is named correctly
- Done 🎉
- Profit 🏦

# Chapter 5: Collaboration with Terraform

### 5.1 Terraform backends


- Backend is a shared storage medium that stores state files
- Backends officially supports blocking
- Blocking is required inorder to prevent multiple user's updating resources at the same time
- Most of the providers support blocking
- We can use S3 as a backend provider
- Backend provider is not in Terraform
Example:

```hcl
terraform {
  required_version = ">=0.14.0"
  backend "s3" {
    # bucket should already exist
    bucket = "my-Terraform-backend"
    key = "sagar-Terraform-resources"
    region = "ap-northeast-1"
    # dynamo db table also should already exist
    dynamodb_table = "sagar-Terraform-lock"
  }
}
```

You must `init` again inorder to change the backend.

Locks are stored in dynamodb table. Whoever acquires the lock first has the precedence of getting the resource.

We can also have remote backend

```hcl
  backend "remote" {
    hostname = "app.Terraform.io"
    organization = "beBit"
    workspace = {
      name = "hello-Terraform"
    }
  }
```
If we change the S3 backend to remote backend, we need to do `terraform init` again which will ask us if we'd like to move the state file from S3 to the remote backend.

### 5.2 Terraform workspaces


- Workspace helps us to create different environment with the same sets of Terraform configurations.
- You can view the list of your Terraform workspaces using the command `terraform workspace list`
- The default workspace name is called `default`
- You can not delete the default workspace
- Execute `terraform workspace --help` to view the workspaces sub-commands

Create a new workspace:

```shell
╰─$ terraform workspace new staging
Created and switched to workspace "staging"!

You're now on a new, empty workspace. Workspaces isolate their state,
so if you run "terraform plan" Terraform will not see any existing state
for this configuration.
```

List the workspaces:

```bash
╰─$ terraform workspace list
  default
* staging

```

Where the `*` is the current one, and we can also use `terraform workspace show` to get the current workspace.

Switch the workspace back to `default`

```bash
╰─$ terraform workspace select default                                                                                                                                                                                              1 ↵
Switched to workspace "default".

```

Deleting the workspace:

```bash
╰─$ terraform workspace delete staging
Deleted workspace "staging"!

```

> Note: The workspace should be clean i.e. destroyed before deleting it.
Learn more here: [https://www.Terraform.io/docs/state/workspaces.html](https://www.Terraform.io/docs/state/workspaces.html)
