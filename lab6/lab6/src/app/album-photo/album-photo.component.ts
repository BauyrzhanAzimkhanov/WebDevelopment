import { Component, OnInit } from '@angular/core';
import {ActivatedRoute} from '@angular/router';
import {Location} from '@angular/common';
import {AlbumsService} from '../albums.service';
import {Photo} from '../photos-matrix';
import {PhotosService} from '../photos.service';

@Component({
  selector: 'app-album-photo',
  templateUrl: './album-photo.component.html',
  styleUrls: ['./album-photo.component.css']
})
export class AlbumPhotoComponent implements OnInit {
  // @ts-ignore
  photos: Photo[];
  temp: any[];
  loading: boolean;
  constructor(private route: ActivatedRoute,
              private location: Location,
              private  photosService: PhotosService) {
    this.photos = [];
    this.temp = [];
    this.loading = true;
  }

  ngOnInit(): void
  {
    // @ts-ignore
    const id = +this.route.snapshot.paramMap.get('id');
    this.getPhotos(id);
    console.log(this.photos);
  }
  getPhotos(id: number): void
  {
    console.log(id);
    this.loading = true;
    this.photosService.getPhotos(id).subscribe((x) => this.photos = x);
    this.loading = false;
    console.log(this.temp);
  }
  goBack(): void
  {
    this.location.back();
  }
}
