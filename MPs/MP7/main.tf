provider "google" {
  credentials = "${file("account.json")}"
  // Change the following line to the correct GCP project!
  project     = "cs199-YOUR_NETID-mp7"
  region      = "us-central1"
}

// Problem 2 - Creating a storage bucket

// Problem 3 - Creating an Instance

// Problem 4 - Creating a Disk and Attaching It

// Problem 5 - Making Your Instance Accessible
